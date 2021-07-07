# 使用者輸入全部資料，再將資料以覆寫方式寫入
# [(id,name)]
# [(1,'Mary'),(2,'John')]
all_data = []
while True:
    id = int(input('Input ID:'))
    if id==-1:
        break
    name = input('Input Name:')
    all_data.append((id,name))
print(all_data)
with open(r'C:\Users\User\Desktop\aaa.txt',mode = 'w') as f:
    #all_lines = [f'{id:4}{name:10}\n' for id,name in all_data]
    all_lines = [f'{id},{name}\n' for id, name in all_data]  #csv格式 讀取
    #print(all_lines,type(all_lines))
    f.writelines(all_lines)