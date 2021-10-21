import cv2
img = cv2.imread(r'C:\Users\User\Desktop\MickyMouse.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('source',img)
print(img.shape)
import numpy as np
kernel = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
from scipy import ndimage
nd_conv_img = ndimage.convolve(img,kernel)
cv2.imshow('nd.convole',nd_conv_img)
print(nd_conv_img.shape)
cv2.waitKey(0)