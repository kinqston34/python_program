#抓台積電股價
import requests
import time
years = [2016,]
for y in years:
    for m in range(1,13):
        param = {'response':'csv','stockNo':'2330','date':''}
        param['date'] = '%d%02d01'%(y,m)
        url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY'
        r = requests.get(url,param)
        with open(r'\%d%02d'%(y,m),mode='w') as f:   #寫檔路徑
            f.writelines(r.text)
        time.sleep(1)