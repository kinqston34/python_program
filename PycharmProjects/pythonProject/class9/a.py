import random
for _ in range(100_0000):
    #ans = int(random.random()*100)
    ans = int(random.random()*99+1)
    if ans > 99 or ans < 1 :
        print('Bug')