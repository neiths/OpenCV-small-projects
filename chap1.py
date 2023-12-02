import cv2
print('Package imported')
# read images-video-webcam

# read images
# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output", img)
# # 0 - infinite, 1 - milisecond
# cv2.waitKey(0)

# read video
# cap = cv2.VideoCapture("Resources/rainyday.mp4")
#
# while True:
#     # success - boolean value
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#


# read webcame
cap = cv2.VideoCapture(0) # default webcame
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("My webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
