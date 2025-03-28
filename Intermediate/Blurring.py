import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")

cv.imshow("Image" , img)

# Kernal Size is Basically number of rows and number of columns

# Averaging

average = cv.blur(img , (7 , 7))
cv.imshow("Average Image" , average)

# Gaussian Blur

blur = cv.GaussianBlur(img , (7 , 7) , 0)
cv.imshow("Blurring Image" , blur)

# Median Blur
median = cv.medianBlur(img , 7)
cv.imshow("Median Blur" , median)

# Bilateral Blur

bilateral = cv.bilateralFilter(img , 10 , 35 , 25)
cv.imshow("Bilateral Blurring"  , bilateral)

cv.waitKey(0)