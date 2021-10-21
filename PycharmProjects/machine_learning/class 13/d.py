from tensorflow import keras
(train_features,train_label),(test_features,test_label) = keras.datasets.mnist.load_data()
print(type(train_features),train_features.shape)
from sklearn import neighbors
clf = neighbors.KNeighborsClassifier()
clf.fit(train_features.reshape(60000,-1),train_label)
print('Fit OK')
idx = 1000
print('real:',test_label[idx])
predict = clf.predict(test_features[idx].reshape(1,-1))
print('predict:',predict)
import matplotlib.pyplot as plt
plt.imshow(test_features[idx],cmap='gray')
plt.show()

print(clf.score(test_features.reshape(10000,-1),test_label))