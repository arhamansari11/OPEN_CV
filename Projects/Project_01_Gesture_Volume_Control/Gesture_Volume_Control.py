import cv2 as cv
import mediapipe as mp
import time
import numpy as np

wCam , hCam = 640 , 720

cap = cv.VideoCapture(0)
cap.set(3 , wCam)
cap.set(4 , hCam)

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
            x1 = y1 = x2 = y2 = 0
            for id , lm in enumerate(handlms.landmark):
                h , w , c = img.shape
                cx , cy = int(lm.x * w) , int(lm.y * h)
                print(id , cx  , cy)
                # if id == 8 or id  == 4:
                #     cv.circle(img , (cx , cy) , 15 , (255 , 0 , 255) , -1)  

                if id == 4:
                    x1 , y1 = cx , cy
                    cv.circle(img , (x1 , y1) , 15 , (255 , 0 , 255) , -1)  
                if id == 8:
                    x2 , y2 = cx , cy
                    cv.circle(img , (x2 , y2) , 15 , (255 , 0 , 255) , -1)  

                if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
                    cv.line(img , (x1 , y1) , (x2 , y2) , (255 , 0 , 255) , 3)


            mpDraw.draw_landmarks(img , handlms , mphands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img , f'FPS : {str(int(fps))}' , (10 , 70) , cv.FONT_HERSHEY_PLAIN , 3 , (255 , 0 , 255) , 3)

    cv.imshow("Image" , img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()