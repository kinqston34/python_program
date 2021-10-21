import numpy as np
element = np.unique([1,1,2])
print(element)
a = np.unique(list('Michael'))
print(a)
print(a.size)
b = np.unique(list('Michelle'))
print(np.intersect1d(a,b).size / np.union1d(a,b).size)