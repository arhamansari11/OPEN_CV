import cv2 as cv
import numpy as np

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale Image" , gray)

# Laplacian
lap = cv.Laplacian(gray ,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("LapLacian" , lap)

sobelx = cv.Sobel(gray , cv.CV_64F , 1 , 0)
sobely = cv.Sobel(gray , cv.CV_64F , 0 , 1)
cv.imshow("Sobel X" , sobelx)
cv.imshow("Sobel Y" , sobely)

combined_sobel = cv.bitwise_or(sobelx , sobely)
cv.imshow("Combine Sobel" , combined_sobel)

cv.waitKey(0)