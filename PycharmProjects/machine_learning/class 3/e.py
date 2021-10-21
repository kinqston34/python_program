l = list(range(0,10))
print(l)

#l = [x**2 for x in l if x < 5]
l = [x**2 if x< 5 else x for x in l ]
print(l)

import numpy as np
arr = np.arange(0,10)
#print(arr < 5)
print(np.where(arr<5,arr**2,arr))
#print(arr[arr<5])