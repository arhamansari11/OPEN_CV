import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image" , gray)

threshold , thresh = cv.threshold(gray , 100 , 250 , cv.THRESH_BINARY)
cv.imshow("Simple Thresholding" , thresh)



cv.waitKey(0)