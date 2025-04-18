import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 2)
drawSpec = mpDraw.DrawingSpec(thickness = 1 , circle_radius = 2)

while True:
    success , img = cap.read()

    imgRGB = cv.cvtColor(img , cv.COLOR_BGR2RGB)

    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, facelms, mpFaceMesh.FACEMESH_TESSELATION , drawSpec , drawSpec)
            for lm in facelms.landmark:
                ih , iw , ic = img.shape
                x , y = int(lm.x * iw) , int(lm.y * ih )
                print(x,y)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img , f'{int(fps)}' , (20 , 70) , cv.FONT_HERSHEY_PLAIN , 3 , (255 , 255 , 0) ,  3 )
    cv.imshow("Video" , img)
    cv.waitKey(1)

