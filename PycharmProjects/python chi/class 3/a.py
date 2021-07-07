import requests
import time
years = [2015]
for y in years:
    for m in range(1,13):
        param = {'response':'csv','stockNo':'2330','date':''}
        param['date'] = '%d%02d01'%(y,m)
        url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date=20160101&stockNo=2330'
        r = requests.get(url,param)
        with open(r'd:',mode='w') as f:
            f.writelines(r.text)