import cv2 as cv
import numpy as np

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")

blank = np.zeros(img.shape, dtype = "uint8")
cv.imshow("Blank" , blank)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(gray , (5 , 5) , cv.BORDER_DEFAULT)

# canny = cv.Canny(blur , 125 , 125)

# cv.imshow("Canny Image" , canny)

# ThresHolding on Image

# ret , thresh = cv.threshold(gray , 125 , 255 , cv.THRESH_BINARY)
# cv.imshow("Thres Image" , thresh)

contours , hierarchies = cv.findContours(thresh , cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank , contours , -1 , (0 , 0 , 255) , 3)
cv.imshow("Contours Drawn" , blank)

cv.waitKey(0)


