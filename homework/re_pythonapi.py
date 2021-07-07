import requests
r = requests.get('https://www.googleapis.com/books/v1/volumes?q=python')
json = r.json()
items = json['items']
i = 1
for obj in items:
    objs = obj['volumeInfo'] #進到volumeInfo
    print('第%d本書:'%i)
    print('title:',objs['title']) #取出全部的title
    print('subtitle:', objs.get('subtitle',""))    #如果有key = subtitle的列印出來
    i+=1

