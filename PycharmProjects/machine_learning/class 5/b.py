import cv2
import numpy as np
a = np.array([1,0])
b = np.array([1,1])
print(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))

from sklearn.metrics.pairwise import cosine_similarity
#print(cosine_similarity(a,b)) 會錯裡面的參數 要是二維的

a = np.reshape(a,(1,-1))
b = np.reshape(b,(1,-1))
print(a,np.ndim(a))
print(b)
print(cosine_similarity(a,b))