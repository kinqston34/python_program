import numpy as np
arr = np.array([4,2,3])
print(arr[::-1])
arr = np.arange(12).reshape(4,3)
print(arr)
print(arr[::-1])
arr = np.eye(4,3)
print(arr)
print(arr[::-1])

import numpy as np
arr = np.array([[1,2],[3,4]])
inverse_eye = np.eye(2,2)[::-1]
print(np.dot(arr,inverse_eye))