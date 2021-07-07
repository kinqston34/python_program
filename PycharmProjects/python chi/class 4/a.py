from bs4 import BeautifulSoup #<網頁有改>
import requests
r = requests.get('http://127.0.0.1:5000')
# print(r.text)
bs = BeautifulSoup(r.text,'html.parser')
# print(bs.html)
# print('----------')
# print(bs.html.body)
# print('----------')
print(bs.html.body.h1.text,type(bs.html.body.h1.text)) #照階層抓(type=str)
print(bs.h1.string,type(bs.h1.string)) #直接抓標籤(type=beautiful的string)
tag = bs.find('h1')
print(tag,type(tag)) #type= bs4.element.Tag
print(tag.text,type(tag.text)) #內文type = str
#當有很多h1 只會先抓到第一個

all_tag = bs.find_all('h1')
print(all_tag,type(all_tag)) #type = bs4.element.ResultSet
for tag in all_tag:
    print(tag.text)
    print(tag['style'],type(tag['style'])) #當有css屬性 當成dict抓取資料 #type=str
# 當有很多相同tag 一次性抓出來用迴圈處理

h1 = bs.find('h1',class_= 'h1css')
print(h1) #指定標籤屬性 #class跟python 保留字相沖
#way1: 加底線
h1 = bs.find('h1',{'class':'h1css'})
print(h1)
#way2: 用字典指定避免相沖

h1 = bs.find(string='Header 2') #找指定內文
print(h1,type(h1))
tag = h1.find_parent()
print(tag,type(tag))

#找層次式的<h1> 先找標的物 在調整指標
h1 = bs.find('h1',{'class':'h1css'})
print(h1,type(h1))
print(h1.h2)
print(h1.find('h2'))
print(h1.find_next('h2'),type(h1.find_next('h2')))
#type = bs.element.Tag



