import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(start=-10,stop=10,step=0.1)
y = (1/np.sqrt(2*np.pi))*np.exp(-np.power(x,2)/2)
import scipy.stats as stats #機率密度函式模組
y1 = stats.norm.pdf(x,loc=0,scale=1)
plt.style.use('')
plt.plot(x,y1,'v--b')
plt.show()