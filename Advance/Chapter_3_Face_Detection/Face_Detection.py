import cv2 as cv
import mediapipe as mp
import time 

cap = cv.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

while True:
    success , img = cap.read()

    imageRGB = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    results = faceDetection.process(imageRGB)
    print(results)
    if results.detections:
        for id , detection in enumerate(results.detections):
            # mpDraw.draw_detection(img , detection)
            # print(id , detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih , iw , ic = img.shape
            bbox = int(bboxC.xmin * iw) , int(bboxC.ymin * ih) , \
                     int(bboxC.width * iw) , int(bboxC.height * ih) 

            cv.rectangle(img , bbox , (255 , 0 ,255 )  , 10)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img , f'FPS : {int(fps)}' , (20 , 70) , cv.FONT_HERSHEY_PLAIN , 3 ,(255 , 0 , 0) , 2)
    cv.imshow("Video" , img)
    cv.waitKey(1)
