import numpy as np
mat_a = np.ones(shape=(100,20))
mat_b = np.ones(shape=(20,120))
mat_c = np.dot(mat_a,mat_b)
print(mat_c.shape)