import cv2 as cv
import numpy as np

blank = np.zeros((400 , 400) , dtype="uint8")

rectangle = cv.rectangle(blank.copy() , (30 , 30) , (370 , 270) , 255 , -1)
circle = cv.circle(blank.copy() , (200 , 200) , 200 , 255 , -1)

# cv.imshow("Circle" , circle)
# cv.imshow("Rectangle" , rectangle)

# Bitwise And ==> InterSection
bitwise_and = cv.bitwise_and(rectangle ,circle )
cv.imshow("BitWise And" , bitwise_and)

# Bitwise Or ==> Merge
bitwise_or = cv.bitwise_or( rectangle  , circle)
cv.imshow("BitWise Or" , bitwise_or)

# Bitwise XOR ==> Now Intersection Region
bitwise_xor = cv.bitwise_xor(rectangle , circle)
cv.imshow("BitWise XOR" , bitwise_xor)

# Bitwise NOT ==> Changes the color of the Image means invert it
bitwise_not = cv.bitwise_not(circle)
cv.imshow("BitWise Not" , bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()
