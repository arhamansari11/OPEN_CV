import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")
cv.imshow("Cats" , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("Gray" , gray)

Canny = cv.Canny(img , 125 , 175)
cv.imshow("Canny Image" , Canny)


cv.waitKey(0)
