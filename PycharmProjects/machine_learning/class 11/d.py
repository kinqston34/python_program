#模擬影像雜訊
import cv2
import numpy as np
img = cv2.imread(r'C:\t2.jpg')
print(img.shape)
cv2.imshow('source',img)
img1 = np.ones_like(img)
noise = cv2.randn(img1,(0,0,0),(120,120,120))
img1 = cv2.addWeighted(img,0.5,noise,0.5,10)
cv2.imshow('noise',img1)
gaussian_blur_img = cv2.GaussianBlur(img1,ksize=(5,5),sigmaX=10)
cv2.imshow('gaussian',gaussian_blur_img)
cv2.waitKey(0)
