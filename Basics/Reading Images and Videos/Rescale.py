import cv2 as cv

img = cv.imread(r"D:\Github\Open CV\Basics\Reading Images and Videos\Photos\cats 2.jpg")



def rescaleFrame(frame , scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)



# For Image Rescaling

# if img is None:
#     print("Path of the Image is not correct...!!!")
# else:
#     frame = rescaleFrame(img)
#     cv.imshow("Cat" , frame)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


# For Video Resizing

# capture = cv.VideoCapture(r"D:\Github\Open CV\Basics\Reading Images and Videos\Videos\dog.mp4")

# while True:
#     isTrue , frame = capture.read()

#     # For Resized Video

#     frame_resized = rescaleFrame(frame , scale=0.1)

#     cv.imshow("Video" , frame_resized)  

#     # For simple Video

#     # cv.imshow("Video" , frame)  

#     if cv.waitKey(20) & 0xff == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
