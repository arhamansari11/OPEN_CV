import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\park.jpg")

# 1. Convert the Image to Gray Image

# gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# cv.imshow("Image" , gray)

# cv.waitKey(0)

# 2. Convert the Image to Blur

Blur = cv.GaussianBlur(img , (7 , 7)  , cv.BORDER_DEFAULT)

# cv.imshow("Blue Image" , Blur)

# cv.waitKey(0)

# 3. Edge Cascade

canny = cv.Canny(Blur , 125 , 175)

cv.imshow("Canny Edges" , canny)

# cv.waitKey(0)

# 4. Dilating the Images

dilate = cv.dilate(canny , (3 , 3) , iterations = 3)

cv.imshow("Dilated" , dilate)

cv.waitKey(0)