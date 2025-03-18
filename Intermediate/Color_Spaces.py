import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")

cv.imshow("Image" , img)

# plt.imshow(img)
# plt.show()

# BGR to GRAY Scale

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

cv.imshow("Gray" , gray)

# BGR TO HSV (Huge Saturation Value)

hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)

cv.imshow("HSV" , hsv)

# BGR TO LAB

lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)

# cv.imshow("Lab Image" , lab)

# BGR to RGB

# rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)

# cv.imshow("RGB" , rgb)

# HSV TO BGR

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

cv.imshow("HSV TO BGR"  , hsv_bgr)

cv.waitKey(0)