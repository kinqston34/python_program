import numpy as np
x = np.array([1,2,3])
y = np.array([1,2])
print(np.convolve(x,y))
print(np.convolve(x,y,mode='valid'))

x = np.array([1,2,3,4,5])
ma = 3
y = np.ones(ma)
print(np.convolve(x,y,mode='valid')/ma)
#捲積 convolve
# ex: [1,4,7,6]
# 運算方式
# 3 2 1
# 0 0 1    第一個: 3*0+2*0+1*1 = 1
# 3 2 1
# 0 1 2   第二個: 3*0+2*1+1*2 = 4
# 3 2 1
# 1 2 0   第三個: 3*1+2*2+1*0 = 7
# 3 2 1
# 2 0 0   第四個: 3*2+2*0+1*0 = 6