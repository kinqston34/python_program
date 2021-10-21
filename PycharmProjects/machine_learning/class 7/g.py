import cv2
import numpy as np
img = np.ones(shape=(600,800,3))
# BGR
img[150:,150:,2] = 255
cv2.imshow('source',img.astype('uint8'))
cv2.waitKey(0)