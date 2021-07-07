#Duplicate Zeros
arr = [1,0,2,3,0,4,5,0]
new = arr
count = 0
b = []
for i in range(len(arr)):
    if arr[i] == 0 and len(arr[:i])+count < len(arr):
        b = new[i+1:len(arr)-1]
        new = new[:i+1]
        new.append(0)
        count += 1
        new = new +b
arr = new
print(arr)