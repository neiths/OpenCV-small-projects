import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)

img = cv2.imread("Resources/lena.png")

# in opencv2 BGR not RGB
imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(3,3),0)
imgCanny = cv2.Canny(img, 100, 100)
imDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imDilation, kernel, iterations=1)

# cv2.imshow("Gray Iamge", imgGray)
# cv2.imshow("Blur Image", imgBlur)
#cv2.imshow("Canny image", imgCanny)

cv2.imshow("dilation image",imDilation)
cv2.imshow("Erode image",imgErode)
cv2.waitKey(0)