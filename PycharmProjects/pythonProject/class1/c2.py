with open (r'C:\Users\User\Desktop\aaa.txt') as f:
    lines = f.readlines()
    for line in lines:
        # id = line[:4]
        # name = line[4:-1]
        # print(id)
        # print(name)
        id,name = line.split(',')   #csv
        print(id,name.strip())
        print(id,name[:-1])
