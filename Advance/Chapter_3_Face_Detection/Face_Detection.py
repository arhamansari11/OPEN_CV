import cv2 as cv
import mediapipe as mp
import time 

cap = cv.VideoCapture(0)
pTime = 0



while True:
    success , img = cap.read()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img , f'FPS : {int(fps)}' , (20 , 70) , cv.FONT_HERSHEY_PLAIN , 3 ,(255 , 0 , 0) , 2)
    cv.imshow("Video" , img)
    cv.waitKey(1)
