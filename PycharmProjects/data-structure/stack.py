top = -1
stack = []
stack_c = 10
def Isempty(top):True if top <0 else False
def Isfull(top):True if top >= stack_c -1 else False
def Push(top,item):
    if top >= stack_c - 1:
        return Isfull(top)
    else:
        top += 1
        stack.append(item)
    return top
def Pop(top):
    if top == -1:
        return Isempty(top)
    else:
        item = stack.pop(top)
        top -= 1
        return item,top

for i in range(5):   #初始化
    id = eval(input())
    student = input()
    top = Push(top,student)
    print("top = %d,stack is :"%top,stack)
print('insert(1) or pop(0)? ,want to end(-9999)?')
while n != -9999:
    if k == 1:
        new_id = eval(input())
        new_student = input()
        top = Push(top,new_student)
        print("top = %d,stack is :"%top,stack)
    elif k == 0:
        item,top = Pop(top)
        print("the pop item:",item)
        print("top = %d,stack is :"%top,stack)
    n = int(input('insert(1) or pop(0)? ,want to end(-9999)?'))

