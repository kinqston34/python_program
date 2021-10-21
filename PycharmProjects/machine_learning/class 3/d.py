l = [1,2,3]
print(l[:2])
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[0:2])
#Fancy Index
print(arr[[0,2,3]])
#Mask Index
print(arr[[True,True,False,False,True]])