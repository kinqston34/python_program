import numpy as np
import cv2
# 顏色切割
img = cv2.imread(r'C:\Users\User\Desktop\color-test.png')
import sys
np.set_printoptions(threshold=sys.maxsize)
print(img)
condi = np.where(img[:,:,1]>150)
img[:,:,:] = 0
img[condi[0],condi[1],0] = 0
img[condi[0],condi[1],1] = 150
img[condi[0],condi[1],2] = 0
cv2.imshow('image',img)
cv2.waitKey(0)