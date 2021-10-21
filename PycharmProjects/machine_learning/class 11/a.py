# scipy
import numpy as np
img = np.arange(1,10).reshape(3,3)
print(img)
# 設計過的kernel
kernel = np.array([[1,1,1],[1,1,0],[1,0,0]])
print(kernel)
from scipy import ndimage
print(ndimage.convolve(img,kernel,mode='constant',cval=0.0))
#會先填充外圍0
# 0 0 0 0 0
# 0 1 2 3 0
# 0 4 5 6 0
# 0 7 8 9 0
# 0 0 0 0 0

# kernel 會先flip 之後才做convole
# 0 0 1
# 0 1 1
# 1 1 1