#!/usr/bin/env python

import cv2
import numpy as np

# load image
img = cv2.imread('smart_nid.jpg')
img= cv2.resize(img,(800,600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,50)
contours, hierarchy = cv2.findContours(adaptive_threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

mx = (0,0,0,0)      # biggest bounding box so far
mx_area = 0
for cont in contours:
    x,y,w,h = cv2.boundingRect(cont)
    area = w*h
    if area > mx_area:
        mx = x,y,w,h
        mx_area = area
x,y,w,h = mx

# Crop and save
roi=img[y:y+h,x:x+w]
cv2.imwrite('Image_crop.jpg', roi)

# Draw bounding box rectangle (debugging)
cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)
cv2.imwrite('Image_cont.jpg', img)

# cv2.imwrite("1.jpg", adaptive_threshold)

cv2.imshow('gray', adaptive_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()