import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")

cv.imshow("Image Show"  , img)

cv.waitKey(0)