from bs4 import BeautifulSoup
import requests
url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY'
y,m = 2016,6
param = {'response':'html','stockNo':'2330','date':''}
param['date'] = '%d%02d01'%(y,m)
r = requests.get(url,param)
bs = BeautifulSoup(r.text,'html.parser')
all_td = bs.find_all('td')
data = []
for td in all_td:
    data.append(td.text)
print(data)
