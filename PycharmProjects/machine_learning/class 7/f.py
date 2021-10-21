# newR = (R × 0.393 + G × 0.769 + B × 0.189)
# newG = (R × 0.349 + G × 0.686 + B × 0.168)
# newB = (R × 0.272 + G × 0.534 + B × 0.131)

# sepia effect

import cv2
import numpy as np
img = cv2.imread(r'c:/')
cv2.imshow('source',img)
#BGR: blue green red 在cv2跟平常的rgb順序不同
sepia_filter = np.array([[.131,.168,.189],[.543,.686,.769],[.272,.349,.393]])
sepia = np.dot(img,sepia_filter)
sepia = np.where(sepia>255,255,sepia)
cv2.imshow('sepia',sepia.astype('uint8'))
cv2.waitKey(0)