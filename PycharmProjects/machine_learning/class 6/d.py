import cv2
import numpy as np
img = cv2.imread(r"C:\Users\User\Desktop\ex1.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Image",img)
inverse_eye = np.eye(img.shape[1],img.shape[0])[::-1]
img_mirror = np.dot(img,inverse_eye).astype('uint8')
print(img_mirror.dtype,img_mirror.shape)
#new_mirror = img_mirror[:,:256]
new_mirror = img_mirror[0:img.shape[0],0:img.shape[1]]
cv2.imshow('Mirror',new_mirror)
cv2.waitKey(0)
