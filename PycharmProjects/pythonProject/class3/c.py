import csv
with open(r'C:\Users\User\Desktop\bbb.txt',mode='w',newline='') as f:
    writer  = csv.DictWriter(f,fieldnames=['id','name'])
    writer.writeheader()
    writer.writerows([{'id': '1', 'name': 'Mary'},{'id': '12', 'name': 'john'}])