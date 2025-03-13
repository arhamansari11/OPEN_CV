import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image" , gray)

# Simple Thresholding

threshold , thresh = cv.threshold(gray , 150 , 250 , cv.THRESH_BINARY)
cv.imshow("Simple Thresholding" , thresh)


threshold , thresh_inv = cv.threshold(gray , 150 , 250 , cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholding Inv" , thresh_inv)


# Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY , 11 , 3)
cv.imshow("Adaptive Thresholding" , adaptive_thresh)

cv.waitKey(0)