#向量乘以純量
import numpy as np
import matplotlib.pyplot as plt
import vector_plt
from vector_plt import plot_a_vector
import seaborn
seaborn.reset_orig()
def vector_scalar_multiple(v,scalar):
    new_v = v*scalar
    return new_v
v = np.array([2,4])
v1 = vector_scalar_multiple(v,5)
v2 = vector_scalar_multiple(v,-2)
v3 = vector_scalar_multiple(v,0)
plt.figure(figsize=(16,4),facecolor='yellow')
plt.subplot(1,3,1)
plot_a_vector(v1[0],v1[1])
plt.subplot(1,3,2)
plot_a_vector(v2[0],v2[1])
plt.subplot(1,3,3)
plot_a_vector(v3[0],v3[1])
plt.show()


