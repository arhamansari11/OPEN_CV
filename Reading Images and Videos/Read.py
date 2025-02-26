import cv2 as cv

# Use double backslashes or raw string to fix the path
img = cv.imread(r"D:\Github\Open CV\Reading Images and Videos\Photos\cats 2.jpg")

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found. Check the file path.")
else:
    cv.imshow("Cat Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()  # Ensure the window closes properly
