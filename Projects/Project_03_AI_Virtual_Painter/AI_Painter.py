import cv2 as cv
import mediapipe as mp
import time
import numpy as np
import os   

folderPath = "Header"
myList = os.listdir(folderPath)
overLaylist = []

for imPath in myList:
    image = cv.imread(f'{folderPath}/{imPath}')
    overLaylist.append(image)

cap = cv.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success , img = cap.read()

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