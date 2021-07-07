import csv   #csv 函式庫
with open(r'C:\Users\User\Desktop\aaa.txt') as f:
    reader = csv.reader(f)
    #print('type(reader)',type(reader))
    next(reader)   #如有表頭 way1
    for element in reader:    #如果有表頭 way2 list(reader)[1:]
        print(type(element))
        print(element[0],element[1],len(element[1]))