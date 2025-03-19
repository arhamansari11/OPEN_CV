import cv2 as cv
import mediapipe as mp
import time
import numpy as np
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam , hCam = 640 , 720

cap = cv.VideoCapture(0)
cap.set(3 , wCam)
cap.set(4 , hCam)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volbar = 400

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
                # print(id , cx  , cy)


                if id == 4:
                    x1 , y1 = cx , cy
                    cv.circle(img , (x1 , y1) , 15 , (255 , 0 , 255) , -1)  
                if id == 8:
                    x2 , y2 = cx , cy
                    cv.circle(img , (x2 , y2) , 15 , (255 , 0 , 255) , -1)  

                if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
                    cv.line(img , (x1 , y1) , (x2 , y2) , (255 , 0 , 255) , 3)

                    cx_center = (x1 + x2) // 2
                    cy_center = (y1 + y2) // 2

                    cv.circle(img , (cx_center , cy_center) , 13 , (255 , 0 , 255) , -1) 

                    length = math.hypot(x2 - x1 , y2 - y1)

                    vol = np.interp(length , [50 , 300] , [minVol , maxVol])
                    volbar = np.interp(length , [50 , 300] , [400 , 150])
                    volume.SetMasterVolumeLevel(vol, None)

                    print(vol)
                    if length < 60:
                        cv.circle(img , (cx_center , cy_center) , 13 , (255 , 255 , 255) , -1) 


            mpDraw.draw_landmarks(img , handlms , mphands.HAND_CONNECTIONS)

    cv.rectangle(img , (50, 150) , (85 , 400) , (0 , 255 , 255) , 3)      
    cv.rectangle(img , (50, int(volbar)) , (85 , 400) , (0 , 255 , 255) , cv.FILLED )      

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img , f'FPS : {str(int(fps))}' , (10 , 70) , cv.FONT_HERSHEY_PLAIN , 3 , (255 , 0 , 255) , 3)

    cv.imshow("Image" , img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()