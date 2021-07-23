def log(func):
    def wrappedFunc():
        print("我")  #會
        return func
    return wrappedFunc
@log
def foo():
    print("inside foo") #不會執行
foo()

