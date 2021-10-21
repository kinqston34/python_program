import numpy as np
mat = np.array([[255,0,0],[0,255,0],[0,0,0]])
print(mat)
condi = np.where(mat>250)
print(condi,type(condi))
print(condi[0],condi[1])
#顯示所有條件下 condi[0]:x座標集合 condi[1]: y座標集合
