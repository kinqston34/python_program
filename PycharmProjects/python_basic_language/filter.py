def isEven(x):
    return x %2 == 0
even_num = list(filter(isEven,[1,2,3,4,5,6]))
print(even_num)

even_num2 = list(filter(lambda x : x % 2 == 0,[1,2,3,4,5,6])) #過濾出條件的需求
print(even_num2)  #filter(func,數組)

n = filter(lambda x : x % 2 == 0,[1,2,3,4,5,6])
print(type(n))