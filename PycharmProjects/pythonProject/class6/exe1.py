from functools import wraps
def type_check(func):
    @wraps(func)
    def inner(*args,**kwargs):
        dict_hints = func.__annotations__
        print('dict_hints',dict_hints)
        print('args',args,type(args))
        for() in zip()
    return inner

@type_check
def add(a:int,b:int)->int:
    return a+b
print(add(1,2))
