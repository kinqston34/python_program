import numpy as np
img1 = np.array([1,1,1],dtype='uint8')
print(type(img1))
img2 = np.array([2,2,2],dtype='uint8')
img3 = img1 + img2
print(img3,img3.dtype)
img3 = img1 - img2
print(img3,img3.dtype)

import cv2
img3 = cv2.addWeighted(img1,1,img2,1,0)
print(img3,img3.dtype)
img3 = cv2.addWeighted(img1,1,img2,-1,0)
print(img3,img3.dtype) #不會overflow 負數會停在0