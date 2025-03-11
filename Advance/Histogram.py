import cv2 as cv
import matplotlib.pyplot as plt    

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")

cv.imshow("Image" , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

cv.imshow("Gray Image" , gray)


gray_hist = cv.calcHist([gray] , [0] , None , [256] , [0 , 256])

plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels.")
plt.plot(gray_hist)
plt.xlim([0 , 256])
plt.show()


cv.waitKey(0)