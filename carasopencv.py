import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('fer2.jpg')
print('Original Dimensions:',img.shape)

while(int(img.shape[0]) > 850 or int(img.shape[0]) > 850):
    scale_percent = 40
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
print('New dimensions:', img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray, 1.05, 6)

if faces is []:
    print('nada encontrado')
    
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (127,0,225), 2)
    cv2.imshow('FaceDetection', img)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()