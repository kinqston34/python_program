import cv2
img = cv2.imread("",cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread("",cv2.IMREAD_GRAYSCALE)

import numpy as np
arr = img.ravel()
arr1 = img1.ravel()
print(np.linalg.norm(img-img1)/img.shape[0]*img.shape(1))