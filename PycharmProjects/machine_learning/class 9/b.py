import numpy as np
mat = np.arange(1,50).reshape(7,7)
print(mat[1:4,2:5])
kernel = np.array([[0.1,0.2,0.3],[0.4,0.5,0.6],[0.7,0.8,0.9]])
print(kernel)
print(np.sum(mat[1:4,2:5]*kernel))
