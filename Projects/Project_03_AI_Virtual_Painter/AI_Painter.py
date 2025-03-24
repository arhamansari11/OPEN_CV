import cv2 as cv
import mediapipe as mp
import time
import numpy as np
import os   

# Read the Images from the folder
folderPath = "Header"
myList = os.listdir(folderPath)
overLaylist = []

for imPath in myList:
    image = cv.imread(f'{folderPath}/{imPath}')
    overLaylist.append(image)

header = overLaylist[0]  # Default header (Pink color selected)

# Video Capture through Camera
cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

mphands = mp.solutions.hands
hands = mphands.Hands(min_detection_confidence=0.85, min_tracking_confidence=0.85)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

brushColor = (255, 0, 255)  # Default: Pink
eraserThickness = 50
xp, yp = 0, 0  # Previous points for smooth drawing

# Create a white canvas
canvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    img[0:130, 0:1280] = header  # Setting up Header Image 

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handlms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

            if len(lmList) > 8:
                x1, y1 = lmList[8]   # Index finger tip
                x2, y2 = lmList[12]  # Middle finger tip

                fingers = []
                if lmList[8][1] < lmList[6][1]:  # Index Finger Up
                    fingers.append(1)
                else:
                    fingers.append(0)
                if lmList[12][1] < lmList[10][1]:  # Middle Finger Up
                    fingers.append(1)
                else:
                    fingers.append(0)

                # **Selection Mode**
                if fingers[0] and fingers[1]:  
                    xp, yp = 0, 0  # Reset previous position to avoid continuous drawing
                    if 250 < x1 < 450:
                        header = overLaylist[0]  # Pink Brush
                        brushColor = (255, 0, 255)
                    elif 500 < x1 < 750:
                        header = overLaylist[1]  # Blue Brush
                        brushColor = (255, 0, 0) 
                    elif 800 < x1 < 1000:
                        header = overLaylist[2]  # Green Brush
                        brushColor = (0, 255, 0)
                    elif 1050 < x1 < 1250:
                        header = overLaylist[3]  # Eraser
                        brushColor = (0, 0, 0)

                # **Drawing Mode**
                if fingers[0] and not fingers[1]:  
                    if xp == 0 and yp == 0:
                        xp, yp = x1, y1
                    if brushColor == (0, 0, 0):
                        cv.line(canvas, (xp, yp), (x1, y1), brushColor, eraserThickness)
                    else:
                        cv.line(canvas, (xp, yp), (x1, y1), brushColor, 15)
                    xp, yp = x1, y1

        mpDraw.draw_landmarks(img , handlms , mphands.HAND_CONNECTIONS)



    imgGray = cv.cvtColor(canvas, cv.COLOR_BGR2GRAY)
    _, imgInv = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY_INV)
    imgInv = cv.cvtColor(imgInv, cv.COLOR_GRAY2BGR)
    img = cv.bitwise_and(img, imgInv)
    img = cv.bitwise_or(img, canvas)

    # FPS Display
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
