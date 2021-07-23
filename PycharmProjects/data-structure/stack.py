#10進位 轉 2進位 , use:stack
stk = []
n = int(input('請輸入要轉成2進位的整數n(10) = '))
while n != 0:
    stk.append(n%2)
    n = int(n/2)
print(stk)
while len(stk) > 0:
    print(stk.pop(),end='')




