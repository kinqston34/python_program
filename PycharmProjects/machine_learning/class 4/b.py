import numpy as np
a = np.arange(16).reshape(4,4)
print(a,a.shape,a.ndim)

b = np.ravel(a) #降成一維
print(b,b.shape,b.ndim)
b = np.reshape(a,-1) #降成一維 #-1:不指定
print(b,b.shape,b.ndim)