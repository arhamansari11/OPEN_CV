import cv2 as cv
import mediapipe as mp
import time
import os

# Initialize WebCam 

cap = cv.VideoCapture(0)
wCam = 640
hCam = 480
cap.set(3 , wCam)
cap.set(4 , hCam)

# Load images for finger count display

folderPath = "Images"
mylist = sorted(os.listdir(folderPath), key=lambda x: int(os.path.splitext(x)[0]))  # Sort numerically
overlayList = [cv.imread(f'{folderPath}/{imgPath}') for imgPath in mylist]

# MediaPipe hands detection

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Landmark IDs for fingertips (Thumb is handled separately)

finger_tips = [4, 8, 12, 16, 20]

pTime = 0
cTime = 0

while True:

    success , img = cap.read()
    imgRGB = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    finger_count = 6 # Default to no fingers (index 6 in images)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            lmList = []
            h , w , c = img.shape
            for id , lm in enumerate(handlms.landmark):
               cx , cy = int(lm.x * w) , int(lm.y * h)
               lmList.append((cx, cy))

            if lmList:
                fingers = []
                if lmList[finger_tips[0]][0] > lmList[finger_tips[0] - 1][0]:
                    fingers.append(1)  # Open
                else:
                    fingers.append(0)  # Closed

            for i in range(1, 5):
                    if lmList[finger_tips[i]][1] < lmList[finger_tips[i] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                
            finger_count = fingers.count(1) if fingers.count(1) > 0 else 6

        mpDraw.draw_landmarks(img , handlms , mpHands.HAND_CONNECTIONS)

    if 1 <= finger_count <= 6:
        resized_overlay = cv.resize(overlayList[finger_count - 1], (200, 200)) 
        img[0:200, 0:200] = resized_overlay


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img , f'FPS: {str(int(fps)) }' , (400 , 70) , cv.FONT_HERSHEY_PLAIN , 3 , (255 , 0 , 255) , 3)
    cv.putText(img, f'Count: {finger_count if finger_count != 6 else 0}', (50, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)


    cv.imshow("Fingers Counter" , img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()