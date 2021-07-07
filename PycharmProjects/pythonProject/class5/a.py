weight = [96,87,110]
height = [1.74,1.89,1.85]
for w,h in zip(weight,height):
    print(w/h**2)

import numpy as np     #numpy 可以直接將容器拿來當變數使用
weight = np.array([96,87,110])
height = np.array([1.74,1.89,1.85])
print(weight/height**2)
