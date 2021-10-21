import numpy as np
arr = np.array([1,2])
print(arr.dtype)  #python 預設 int64 , numpy 預設 int32
x = arr + 255
print(x,type(x))

arr = np.array([1,2],dtype='uint8')
print(arr.dtype)
x = arr + 255
print(x,type(x))
x = 1
print(x,type(x))