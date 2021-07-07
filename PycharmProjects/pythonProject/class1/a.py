#decorator
from functools import wraps
def type_check(func):
    @wraps(func)
    def inner(*args,**kwargs):
        dict_hints = func.__annotations__
        print('args',args)
        print ('kwargs',kwargs)
        print('dict_hints',dict_hints)
        print('dict_hints.items',dict_hints.items())
        # 處理參數以 args 送入, add(1,2)
        for (func_param_name,func_param_type),arg in zip(dict_hints.items(),args):
            print('func',func_param_name,func_param_type)
            print('arg',arg)
            if not isinstance(arg,func_param_type):
                print('func:',func.__name__,'parameter:',func_param_name,'must be ',func_param_type,'but',type(arg))
                return None
        # 處理參數以kwargs 送入,add(a=1,b=2)
        for func_param_name,func_param_type in dict_hints.items():
            if func_param_name !='return' and kwargs.get(func_param_name,0):
                if not isinstance(kwargs[func_param_name],func_param_type):
                    print('func:',func.__name__,'parameter:',func_param_name,'must be',func_param_type,'but',type(kwargs[func_param_name]))
                    return None
        return_value = func(*args,**kwargs)
        return return_value
    return inner
@type_check
def add(a:int,b:int)->int:
    return a+b
print(add(1,'2'))
print('OK')


