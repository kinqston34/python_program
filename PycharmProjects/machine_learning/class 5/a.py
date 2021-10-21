import cv2
import numpy as np
a = np.array([1,2,3,4])
b = np.array([0,2,3,4])
diff = a-b
print(type(diff))
#盡量不要繞迴圈
# vectorization
print(np.count_nonzero(diff)) #方法
print("Similarity:",1-np.count_nonzero(diff)/diff.size)