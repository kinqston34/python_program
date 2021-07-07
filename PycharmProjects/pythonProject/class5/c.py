import numpy as np
arr = np.array([1,2,3])
# 物件導向->物件.屬性/物件.方法()
print(arr.mean())
# Function Programming
print(np.mean(arr))
print(np.std(arr))
print(np.std(arr,ddof=1)) 
