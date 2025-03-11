import cv2 as cv
import matplotlib.pyplot as plt    
import numpy as np

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats 2.jpg")
# cv.imshow("Image" , img)


# Gray Computing Histogram

# gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# # cv.imshow("Gray Image" , gray)


# blank = np.zeros(img.shape[:2] , dtype = "uint8")
# circle = cv.circle(blank , (img.shape[1] // 2 , img.shape[0] // 2) , 100 , 255 , -1)

# mask = cv.bitwise_and(gray , gray , mask=circle)

# cv.imshow("Masking" , mask) 


# gray_hist = cv.calcHist([gray] , [0] , mask , [256] , [0 , 256])

# plt.figure()
# plt.title("GrayScale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels.")
# plt.plot(gray_hist)
# plt.xlim([0 , 256])
# plt.show()


# Color Computing Histogram

plt.figure()
plt.title("ColorScale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels.")
colors = ('b' , 'g' , 'r')
for i , col in enumerate(colors):
    hist = cv.calcHist([img] , [i] , None , [256] , [0 , 256])
    plt.plot(hist , color = col)
    plt.xlim([0 , 256])

plt.show()

cv.waitKey(0)