import cv2 as cv
import numpy as np


img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats 2.jpg")
blank = np.zeros(img.shape[:2] , dtype = 'uint8')

cv.imshow("Image" , img)

b , g , r = cv.split(img)


blue = cv.merge([b , blank , blank])
green = cv.merge([blank , g , blank])
red = cv.merge([blank , blank , r])

cv.imshow("Blue" , blue)
cv.imshow("Red" , red)
cv.imshow("Green" , green)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

merge = cv.merge([ b , g , r ])
cv.imshow("Merge Image" , merge)

cv.waitKey(0)
