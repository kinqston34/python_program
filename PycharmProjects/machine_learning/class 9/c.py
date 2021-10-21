import cv2
import numpy as np
kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
print(kernel)
img = cv2.imread(r'C:\t2.jpg',cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape
newImage = np.ones(shape=(rows-2,cols-2))
for r in range(rows - 2):
    for c in range(cols - 2):
        newImage[r][c] = np.sum(img[r:r+3,c:c+3]*kernel)
cv2.imshow('source',img)
cv2.imshow('newImage',newImage.astype('uint8'))
cv2.waitKey(0)