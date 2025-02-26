import cv2 as cv
import numpy as np

# Blank Image

blank = np.zeros((500 , 1000  , 3)  , dtype = "uint8")
# cv.imshow("Blank Image" , blank)
# cv.waitKey(0)



# 1. Paint the image a certain color

# blank[:] = 255 , 0 , 0

# cv.imshow("Blue Image"  , blank)
# cv.waitKey(0)



# # 2. Draw a RectAngle Image

# cv.rectangle(blank , (0,0) , (250 , 500) , (255 , 0 , 0) , thickness = -1 )

# cv. imshow("RECATANGLE"  , blank)
# cv.waitKey(0)

# 3. Draw a Circle on the Image

# cv.circle(blank , (250 , 250)  , 40 , (0  , 0 , 255) , thickness = -1)

# cv.imshow("Cicle Image"  , blank)

# cv.waitKey(0)


# 4. Draw a Line

# cv.line(blank , (0 , 0) , (250 , 250) , (0 , 0 , 255) , thickness = 2)

# cv.imshow("Line" , blank)

# cv.waitKey(0)


# 5. Write Text on Image

cv.putText(blank , "Hello my name is Muhammad Arham...!!!" , (0 , 225) , cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0 , 255 , 0) , 2)

cv.imshow("Text on Image" , blank)

cv.waitKey(0)