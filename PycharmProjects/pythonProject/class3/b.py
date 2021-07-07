import csv   #csv 函式庫
with open(r'C:\Users\User\Desktop\aaa.txt') as f:
    reader = csv.DictReader(f,delimiter='|',quotechar = '#')  #有表頭 way3  如果逗號變成其他符號下delimiter
    for dic in reader:                                        #如果文字中有"" 則函式內建刪除
        print(type(dic))                                      #如果文字前後有其他符號 quotechar 
        print(dic['id'],dic['name'])