import numpy as np
data = np.genfromtxt(r'C:\Users\User\Desktop\elcand.csv',encoding='UTF-8',delimiter=',',dtype=None,names = 'c0,c1,c2,c3,c4,c5,c6,c7,c8,birthYear,c10,c11,c12,c13,elected,c15')
# dtype : data type
# 數值處理 Vector(向量),Matrix(矩陣)
# dtype=none : 不轉型 (預設是float)
print(data['birthYear'])
age = 99 - data['birthYear']
print(np.mean(age))
print(np.std(age))
