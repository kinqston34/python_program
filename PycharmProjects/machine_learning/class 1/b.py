import cv2

img = cv2.imread(r'c:\license_plate.jpg')
print(type(img),img.shape)
img = cv2.imread(r'c:\license_plate.jpg', cv2.IMREAD_GRAYSCALE)
print(type(img),img.shape)
import numpy as np
l = [1,'A']
print(l)
arr = np.array([1,'A'])
print(arr)
for element in arr:
    print(element,type(element))