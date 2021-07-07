from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20210701&stockNo=2330")
bs = BeautifulSoup(r.text,'html.parser')
#tbody = bs.find('tbody')   #會出現空白行，無法躲避
rs_tr = bs.select('tbody tr') #用select 解決如標籤中出現空白行 可以去掉
#print(tbody,type(tbody))
for tr in rs_tr:
    l = []
    rs_td = tr.select('td')
    #print(rs_td[0])
    for td in rs_td:
        #l.append(td.text)
        l.append(f'"{td.text}"')
    with open(r'C:\Users\User\Desktop\2021.07.txt',mode='a') as f:
        #f.writelines(l)
        f.writelines(','.join(l))
        f.write('\n')

# import bs4
# for t in tbody:
#     if isinstance(t,bs4.element.Tag):
#         print(t,type(t))
