def func(x,y,z):
    return x+y+z

print(func(1,2,3))
#---------------------
func2 = lambda x,y,z : x+y+z
print(func2(2,4,6))

#---------------------
def func(n):
    if n % 2 == 0:
        print("偶數")
    else:
        print("奇數")

func2 = lambda n : "偶數" if n % 2 == 0 else "奇數"
print(func2(7777))

