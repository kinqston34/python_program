import cv2
import numpy as np
img = np.array([[100,200],[150,250]],dtype='uint8')
print(img)
return_threshold,result = cv2.threshold(img,thresh=150,maxval=255,type=cv2.THRESH_BINARY)
print(return_threshold)
print(result)