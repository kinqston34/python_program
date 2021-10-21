import cv2
import numpy as np
img = np.arange(1,10).reshape(3,3).astype('uint8')
kernel = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
print(cv2.filter2D(src=img,ddepth=-1,kernel = kernel))
print(cv2.filter2D(src=img,ddepth=-1,kernel = kernel,anchor=(0,0)))
img = np.arange(1,10).reshape(3,3).astype('uint8')
img[1,2] = 20
img[2,2] = 30
print(img)
kernel = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
print(cv2.filter2D(src=img,ddepth=-1,kernel=kernel,anchor=(0,0)))
