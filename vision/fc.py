import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,img = cap.read()
    cv2.imshow('input', img)
    k = cv2.waitKey(10)
    if k == 27:
        break
    
