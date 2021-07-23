import matplotlib.pyplot as plt
import seaborn
from coordinate_set import plot_a_vector
seaborn.reset_orig()
plt.subplot(2,2,1)
plot_a_vector(8,8)
plt.subplot(2,2,2)
plot_a_vector(-5,6)
plt.subplot(2,2,3)
plot_a_vector(-3,-6)
plt.subplot(2,2,4)
plot_a_vector(8,-5)
plt.show()
