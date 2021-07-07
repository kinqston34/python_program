import time
import requests
start = int(input('從民國幾年開始'))
end = int(input('到民國幾年結束'))
def u(start,end):       #修改範圍內的所有網址，並回傳
    list_u = []     #url list
    list_n = []     #file_name list
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date=20160101&stockNo=2330'
    p = url.split('&')
    date = p[1].split('=')
    stockNo = p[2].split('=')
    year = date[1][0:4]
    month = date[1][4:6]
    for i in range(start, end+1):
        for j in range(1, 13):
            y = i + 1911
            new_url = p[0] + '&' + date[0] + '=' + str(y) + '{:02}'.format(j) + date[1][6:] + '&' + p[2]
            name = str(y)+'{:02}'.format(j) +'.txt'
            list_u.append(new_url)
            list_n.append(name)
    return list_u,list_n

url_l,url_n= u(start,end)
print('url_l: ',url_l)
print('url_n:',url_n)
for i in range(len(url_l)):
    r = requests.get(url_l[i])      #讀取回傳需求
    time.sleep(1)
    with open(url_n[i], 'w', encoding='UTF-8') as f:        #寫檔
        f.write(r.text)



