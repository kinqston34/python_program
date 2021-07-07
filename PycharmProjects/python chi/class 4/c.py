#執行時間太慢(發現是網站慢)，分段去處理
import requests
from bs4 import BeautifulSoup
import time
def get_stroke(s):
    start = time.time()
    r = requests.get('http://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint='+s)
    print('1',time.time() - start)
    start = time.time()
    bs = BeautifulSoup(r.text,'html.parser')
    navi_str = bs.find(string='kTotalStrokes')   #找到特定內容字
    print('2', time.time() - start)
    return int(navi_str.find_next('code').text)  #往下找到code 需要裡面的筆畫

k = ['陳','王','林'] #想以筆畫排序
k.sort(key=get_stroke)
print(k)


# way1:將資料儲存至資料庫(MSSQL,MySQL) 排序
# way2:用unicode網站的查詢碼

