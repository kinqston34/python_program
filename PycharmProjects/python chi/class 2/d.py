s = 'ABC'
print(s,type(s))
a = s.encode()     #str->bytes
print(a,type(a))
x = a.decode('UTF-8') #bytes ->str
print(x,type(x))
