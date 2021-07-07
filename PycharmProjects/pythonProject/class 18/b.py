from bs4 import BeautifulSoup
import requests
r = requests.get('http://127.0.0.1:5000/')
bs = BeautifulSoup(r.text,'html.parser')
# print(bs.h1,type(bs.h1))
# print(bs.h1.text,type(bs.h1.text))
# print(bs.h1.string,type(bs.h1.string))
print(bs.find('h1'),type(bs.find('h1')))
print(bs.find('h1',style='color:tomato'))
print(bs.find('h1',class_ = 'h1css'))
print(bs.find('h1',{'class': 'h1css'}))
print(bs.find(text = 'Header 1'))
# print(bs.find_all('h1'),type(bs.find_all('h1')))
# all_tag = bs.find_all('h1')
# for tag in all_tag:
#     print(tag,type(tag))
#     print(tag['style'], type(tag))