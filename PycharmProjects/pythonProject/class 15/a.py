import pandas as pd
df1 = pd.read_csv(r'C:\Users\User\Desktop\dataset1.txt')
df2 = pd.read_csv(r'C:\Users\User\Desktop\dataset2.txt')
df3 = pd.read_csv(r'C:\Users\User\Desktop\dataset3.txt')
df4 = pd.read_csv(r'C:\Users\User\Desktop\dataset4.txt')
import matplotlib.pyplot as plt
plt.subplot(2,2,1)
plt.scatter(df1.x,df1.y)
plt.subplot(2,2,2)
plt.scatter(df2.x,df2.y)
plt.subplot(2,2,3)
plt.scatter(df3.x,df3.y)
plt.subplot(2,2,4)
plt.scatter(df4.x,df4.y)
plt.show()

