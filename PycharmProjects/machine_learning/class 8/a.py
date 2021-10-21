import cv2
import numpy as np
# img1 = np.array([[1,2],[3,4]],dtype='uint8')
# img2 = np.array([[1,2],[3,4]],dtype='uint8')
img1 = cv2.imread(r'c:\t2.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'c:\t2.jpg',cv2.IMREAD_GRAYSCALE)
img1 = img1.astype('int64')
img2 = img2.astype('int64')
img1 = img1.ravel()
img2 = img2.ravel()
print(np.dot(img1,img2)/(np.linalg.norm(img1)*np.linalg.norm(img2)))
print(np.dot(img1,img2)) #數字過小 uint8 造成overfloat,cv2預設是uint8
#真實圖片上面手動寫的會出現誤差 底下cosine_similarity是正確的(已確定公式正確)
# img1 = np.array([[1,2],[3,4]],dtype='uint8')
# img2 = np.array([[1,2],[3,4]],dtype='uint8')
# from sklearn.metrics.pairwise import cosine_similarity
# img1 = np.reshape(img1,(1,-1))
# img2 = np.reshape(img2,(1,-1))
# print(cosine_similarity(img1,img2))