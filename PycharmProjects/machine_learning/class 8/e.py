import pytesseract
#光學辨識模組
import cv2
img = cv2.imread(r'C:\Users\User\Desktop\capcha3.jpg',cv2.IMREAD_GRAYSCALE)# 利用灰階有可能可以增加辨識率
cv2.imshow('source',img)
import numpy as np
# Image Binarization (影像二值化)
img1 = np.where(img > 150,255,0)
img1 = img1.astype('uint8')
cv2.imshow('binary',img1)
cv2.waitKey(0)
text = pytesseract.image_to_string(img)
print(text)