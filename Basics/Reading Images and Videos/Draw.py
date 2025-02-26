import cv2 as cv
import numpy as np

# Blank Image

blank = np.zeros((500 , 500  , 3)  , dtype = "uint8")
# cv.imshow("Blank Image" , blank)
# cv.waitKey(0)



# 1. Paint the image a certain color

# blank[:] = 255 , 0 , 0

# cv.imshow("Blue Image"  , blank)
# cv.waitKey(0)



# 2. Draw a RectAngle Image

cv.rectangle(blank , (0,0) , (250 , 500) , (255 , 0 , 0) , thickness = -1 )

cv. imshow("RECATANGLE"  , blank)
cv.waitKey(0)