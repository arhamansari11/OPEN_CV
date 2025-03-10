import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats.jpg")


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray , (5 , 5) , cv.BORDER_DEFAULT)



canny = cv.Canny(blur , 125 , 125)

cv.imshow("Canny Image" , canny)

contours , hierarchies = cv.findContours(canny , cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)

