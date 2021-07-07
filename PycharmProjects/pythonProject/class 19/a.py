import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-3,3,.1)
import scipy.stats as stats
y = stats.norm.pdf(x,loc=0,scale=1)
#圖例
plt.plot(x,y,label='std=1')
z = stats.norm.pdf(x,loc=1,scale=1.5)
# plt.plot(x,y,label='std=1.5')
# plt.legend(loc = 'upper left')

#subplot
# nrows = 1
# ncols = 2
# index = 1
#
# subplot = plt.subplot(nrows,ncols,index)
# plt.plot(x,y,label = 'std=1')
# plt.legend(loc = 'upper left')
# plt.subplot(122)
# plt.plot(x,z,label = 'std=1.5')
# plt.legend(loc = 'upper left')

#subplots
# fig,(ax0,ax1) = plt.subplots(nrows = 1,ncols = 2,sharey=True)
# ax0.set_title('Axes 1')
# ax0.plot(x,y,label = 'std=1')
# ax0.legend(loc='right')
# ax1.set_title('Axes 2')
# ax1.plot(x,y,label = 'std=1.5')
# ax1.legend(loc='right')
# fig.suptitle('Standard Deviation')

#主副圖
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# ax1.plot(x,y)
#
# ax2 = fig.add_axes([0.2,0.6,0.2,0.2])
# z = np.sin(x)
# ax2.plot(x,z)

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\SimSun.ttc",size=14)
print(type(font))
plt.title('學習時間',fontproperties=font)
# plt.xlabel("Time")
# plt.ylabel("Growth")
# plt.plot(x,y)
plt.show()