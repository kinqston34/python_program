import numpy as np
import scipy.stats as stats
x = np.arange(-3,3,.01)
y = stats.norm.pdf(x,loc = 0,scale = 1)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()