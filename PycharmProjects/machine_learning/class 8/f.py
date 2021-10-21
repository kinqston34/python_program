import numpy as np
mat = np.array([[0,0,255,0],[0,0,0,0]])
print(mat)
print(np.where(mat>200,999,-3))