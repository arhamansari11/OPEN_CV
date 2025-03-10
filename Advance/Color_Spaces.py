import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\boston.jpg")

cv.imshow("Image" , img)

cv.waitKey(0)