import cv2
import numpy as np
img = cv2.imread(r'C:/t2.jpg',cv2.IMREAD_GRAYSCALE)
kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
np_con_img = np.convolve(img.ravel(),kernel.ravel(),mode='same')
# np.convolve 只支援一維
np_con_img = np_con_img.reshape(img.shape) #要再把維度轉回來
cv2.imshow('source',img)
cv2.imshow('np.convolve',np_con_img.astype('uint8'))
cv2.waitKey(0)