arr = [2,3,45,12,1]

def bubble_sort(arr):
    def swap(x,y):
        arr[x],arr[y] = arr[y],arr[x]
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                swap(j,j+1)
    return arr
print(bubble_sort(arr))


