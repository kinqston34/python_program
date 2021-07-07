url = 'https://www.twse.com.tw/exchangeReport/FMSRFK?response=csv&date=20160101&stockNo=2330'
p = url.split('&')
date = p[1].split('=')
stockNo = p[2].split('=')
year = date[1][0:4]
month = date[1][4:6]
print(month)
for i in range(105,108):
    for j in range(1,13):
        y = i+1911
        new_url = p[0]+'&'+date[0]+'='+str(y)+'{:02}'.format(j)+date[1][6:]+'&'+p[2]
        print(new_url)





