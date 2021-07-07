import csv   #csv 函式庫
with open(r'C:\Users\User\Desktop\aaa.txt') as f:
    reader = csv.DictReader(f)
    for dic in reader:
        print(dic)
