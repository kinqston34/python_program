from bs4 import BeautifulSoup
import requests
r = requests.get('http://127.0.0.1:5000/')
bs = BeautifulSoup(r.text,'html.parser')
print(bs.html)
print('-----------------')
print(bs.html.body)
print('-----------------')
print(bs.html.body.h1)  #way1 照結構一層層往下
