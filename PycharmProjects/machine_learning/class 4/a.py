import numpy as np
a = np.array([3,4])
#Linear Algebra
print(np.linalg.norm(a),type(np.linalg.norm(a)))

b = np.arange(16)
print(b,b.shape)
c = b.reshape(4,4)
print(c,c.shape)