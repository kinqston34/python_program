import numpy as np
#identity matrix
i = np.eye(3)
print(i)

a = np.arange(9).reshape(3,3)
print(a)
print(np.dot(a,i))
