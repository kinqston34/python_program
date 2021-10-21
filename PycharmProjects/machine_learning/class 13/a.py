import cv2
face_cascade = cv2.CascadeClassifier(r'C:\Users\User\anaconda3\library\etc\haarcascades\haarcascade_frontalface_default.xml')
img = cv2.imread(r'C:\t3.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#轉灰階
faces = face_cascade.detectMultiScale(gray)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),color = (255,0,0),thickness=2) #畫一個四邊形框框
cv2.imshow('img',img)
cv2.waitKey(0)
