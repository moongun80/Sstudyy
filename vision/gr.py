import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thrsh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('input', img)
    cv2.imshow('gray', gray)
    cv2.imshow('blur', blur)
    cv2.imshow('threshold', thrsh1)
    k = cv2.waitKey(10)
    if k == 27:
        break
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    if (area>max_area):
        max_area = area
        ci = i
        cnt = contours[ci]
        hull = cv2.convexHull(cnt)

drawing = np.zeros(img.shape, np.unit8)
cv2.drawContours(drawing, [cnt], 0, (0,255,0), 2)
cv2.drawContours(drawing, [hull], 0, (0,0,255), 2)
