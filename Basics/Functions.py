import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\park.jpg")

# 1. Convert the Image to Gray Image

# gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# cv.imshow("Image" , gray)

# cv.waitKey(0)

# 2. Convert the Image to Blur

# Blur = cv.GaussianBlur(img , (1 , 1)  , cv.BORDER_DEFAULT)

# cv.imshow("Blue Image" , Blur)

# cv.waitKey(0)