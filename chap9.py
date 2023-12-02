import cv2

faceCascade= cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/lena.png')
imgResize = cv2.resize(img,(400,500))
imgGray = cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(imgResize,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result", imgResize)
cv2.waitKey(0)