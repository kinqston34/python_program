from sklearn import neighbors
clf = neighbors.KNeighborsClassifier(n_neighbors=1)
import numpy as np
features = np.array([[3,4],[3.1,4],[2.9,4],[-1,1],[-0.9,1]])
print(features)
label = np.array([1,1,1,0,0]) #資料及編號
clf.fit(features,label)
print(clf.predict([[2.9,4.1]])) #預測點
print(clf.predict([[-1.1,1.2]]))
# 預設取五個最近資料集去投票，所以要將資料集設定為1 (所以要設定為最近的那一個做比對)
# 對於各種資料集的狀況，詳細看文件去判斷

