import cv2
import numpy as np
img = cv2.imread(r'C:/t2.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('source',img)
img_sobel_dx = cv2.Sobel(src=img,ddepth=-1,dx=1,dy=0)
cv2.imshow('soble,dx=1',img_sobel_dx)
img_sobel_dy = cv2.Sobel(src=img,ddepth=-1,dx=0,dy=1)
cv2.imshow('soble,dy=1',img_sobel_dy)
img_sobel = cv2.Sobel(src=img,ddepth=-1,dx=1,dy=1)
cv2.imshow('soble',img_sobel)
cv2.waitKey(0)
