import numpy as np
a = np.array([[1,2],[2,3]])
print(a)
a_1 = np.linalg.inv(a)
print(a_1)
eql = np.array([5,8])
print(np.dot(a_1,eql))