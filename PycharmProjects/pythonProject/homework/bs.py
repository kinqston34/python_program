from bs4 import BeautifulSoup
import requests
url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY'
y,m = 2021,6
param = {'response':'html','stockNo':'2330','date':''}
param['date'] = '%d%02d01'%(y,m)
r = requests.get(url,param)
bs = BeautifulSoup(r.text,'html.parser')
all_td = bs.select('td')
count = 1
for td in all_td:
    with open(r'C:\Users\User\Desktop\2021.06.txt', mode='a') as f:
        f.writelines(f'"{td.text}"')
        f.write(',')
        if count % 9 == 0:
            f.write('\n')
    count += 1