import pandas as pd
#df = pd.DataFrame({'id':[1,2],'name':['Mary','John']})
dfs = pd.read_html('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20210701&stockNo=2330'
                   ,skiprows=1,header=0)

for df in dfs:
    print(df,type(df))
    print(df.columns)
    print(df['收盤價'])