import cv2
img = cv2.imread(r'c:/t2.jpg')
cv2.imshow('cv2',img)
print(img.ndim,img.shape)
img_gray = cv2.imread(r'c:/t2.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('cv2 gray',img_gray)
print(img_gray.ndim,img_gray.shape)

import numpy as np
gray_kernel = np.ones(shape = (3,3))/3.0
print(gray_kernel)
my_gray = np.dot(img,gray_kernel)
print(my_gray.ndim,my_gray.shape)
cv2.imshow('my gray',my_gray.astype('uint8'))
cv2.waitKey(0)