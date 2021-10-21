import numpy as np
img = np.arange(3*2).reshape(3,2)
print(img)
print(np.flip(img,axis=1))

import cv2
img = cv2.imread(r'C:\Users\User\Desktop\ex1.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('source',img)
#flip_img = np.flip(img,axis=1)
flip_img = cv2.flip(img,flipCode=1)
cv2.imshow('flip',flip_img)
cv2.waitKey(0)
