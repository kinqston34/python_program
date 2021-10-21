import cv2
import numpy as np
img = np.ones(shape=(300,600),dtype="uint8")
img = img *155
img = img.astype('uint8')
print(img.dtype)
cv2.imshow('image',img)
cv2.waitKey(0)