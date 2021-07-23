#decorator 如果有回傳值
import time
def display_time(func):
    def wrapper(*args):  #將參數帶入
        t1 = time.time()
        result = func(*args)   #使用參數
        t2 = time.time()
        print('Total time:{:.4} s'.format(t2-t1))
        return result
    return wrapper

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i ==0:
                return False
        return True

@display_time
def count_prime_nums(max): #如果有帶參數，必須將參數傳到decorator
    count = 0
    for i in range(2,max):
        if is_prime(i):
            count += 1
    return count
count = count_prime_nums(10000)
print(count)