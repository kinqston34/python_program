import cv2
import numpy as np
img = cv2.imread(r'c:\t2.jpg',cv2.IMREAD_GRAYSCALE)
kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
new_image = cv2.filter2D(src = img,ddepth=-1,kernel=kernel)
cv2.imshow('cv2.filter2d',new_image)
cv2.waitKey(0)