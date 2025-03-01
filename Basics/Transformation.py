import cv2 as cv
import numpy as np

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats 2.jpg")

# Translate Image

def translate(img , x , y):
    tranMat = np.float32([[1 , 0 , x] , [0 , 1 , y]])
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , tranMat , dimensions)


#  -x ---> left
#  -y ---> up
#  +x --> right
#  +y --> bottom

tranlated = translate(img , 100 , 100)
cv.imshow("Tranlated Image" , tranlated)


# Rotate Image

def rotate(img , angle , rotPoint = None):
    (height , width) = img.shape[:2]
    if rotPoint == None:
        rotPoint = (width // 2 , height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint , angle , 1.0)
    dimensions = (width , height)

    return cv.warpAffine(img , rotMat , dimensions)


rotated = rotate(img , -45)

rotated_rotated = rotate(rotated , -45)

cv.imshow("Rotated" , rotated)

cv.imshow("Rotated Rotated" , rotated_rotated)

cv.waitKey(0)

