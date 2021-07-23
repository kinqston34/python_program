#str和repr差別
class Printer:
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return str(self.value)
# 用此方法必須要用迴圈才能取出內容值
objs = [Printer(2),Printer(3)]
for x in objs:
    print(x)
print(objs)
#----------------------------------
class Printer1:
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return str(self.value)
# 用此方法必須要用迴圈才能取出內容值
print('----------------------------')
objs = [Printer1(2),Printer1(3)]
for x in objs:
    print(x)
print(objs)