from tensorflow import keras
(train_features,train_label),(test_features,test_label) = keras.datasets.mnist.load_data()
print(type(train_features),train_features.shape)
idx = 100
print(train_label[idx])
import matplotlib.pyplot as plt
plt.imshow(train_features[idx],cmap='gray')
plt.show()