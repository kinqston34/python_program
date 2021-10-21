import numpy as np
arr = np.array([1,2],dtype = 'int32')
print(arr.dtype)
print(arr.itemsize)
# 計算arr 在記憶體內的總容量(元素個數*元素型態容量)
# 2 * 4 = 8
print(arr.nbytes)