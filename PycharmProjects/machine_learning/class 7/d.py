import numpy as np
img = np.arange(2*4*3).reshape(2,4,3)
print(img)
print(img[0,1,1])
vector = np.arange(1,10).reshape(3,3)
print(vector)
print(np.dot(img,vector))