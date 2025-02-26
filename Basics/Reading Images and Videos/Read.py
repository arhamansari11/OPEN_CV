import cv2 as cv


# For Reading Image

# # Use double backslashes or raw string to fix the path
# img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats 2.jpg")

# # Check if the image was loaded successfully
# if img is None:
#     print("Error: Image not found. Check the file path.")
# else:
#     cv.imshow("Cat Image", img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()  # Ensure the window closes properly


# For Reading Video

# Video Path

capture = cv.VideoCapture(r"D:\Github\Open CV\Basics\Reading Images and Videos\Videos\dog.mp4")

# Read the Image Frame by Frame

while True:
    isTrue , frame = capture.read()

    cv.imshow("Video"  , frame)

    if cv.waitKey(20) & 0xFF == ord("a"):
        break


capture.release()
cv.destroyAllWindows()  


