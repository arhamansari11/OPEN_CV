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

header = overLaylist[0]

# Video Capture through Camera

cap = cv.VideoCapture(0)
cap.set(3 , 1280)
cap.set(4 , 720)


mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:

    # Setting up Header Image There.

    success , img = cap.read()
    img = cv.flip(img , 1)
    img[0:130 , 0:1280] = header    


    # Check which fingers are up

    # If selection mood - When two fingers are up

    # If we have the drawing mood -> When the index finger is up

    imgRGB = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id , lm in enumerate(handlms.landmark):
                h , w , c = img.shape
                cx , cy = int(lm.x * w) , int(lm.y * h)
                if id == 8:
                    cv.circle(img , (cx , cy) , 25 , (255 , 0 , 255) , -1)
            mpDraw.draw_landmarks(img , handlms , mphands.HAND_CONNECTIONS)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img , str(int(fps)) , (10 , 70) , cv.FONT_HERSHEY_PLAIN , 3 , (255 , 0 , 255) , 3)

    cv.imshow("Image" , img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()