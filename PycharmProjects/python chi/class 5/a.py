from bs4 import BeautifulSoup
import requests
r = requests.get('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20210701&stockNo=2330')
bs = BeautifulSoup(r.text,'html.parser')
#tbody = bs.find('tbody')
import bs4
rs_tr = bs.select('tbody tr')
for tr in rs_tr:
    rs_td = tr.select('td')
    l = []
    for td in rs_td:
        l.append(f'"{td.text}"')
    with open(r'',mode = 'a') as f:
        f.writelines(','.join(l))
        f.write('\n')
# for t in tbody:
#     if isinstance(t,bs4.element.Tag):
#         print(t)
#         print(type(t))
#         print('--------------------------')
