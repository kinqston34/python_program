#Test a.py 大範圍測試到網頁網路上 並且回應出程式需求
import requests
param = {'a':1,'b':2}
r = requests.get('http://127.0.0.1:8080/add',param) #要開啟才能執行
print(r.text,type(r.text))

r = requests.post('http://127.0.0.1:8080/add',param) #要開啟才能執行

print(r.text,type(r.text))