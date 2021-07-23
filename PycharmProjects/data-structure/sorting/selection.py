arr = [2,3,45,12,1]
def selection_sort(arr):
    def swap(x,y):
        arr[x],arr[y] = arr[y],arr[x]

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                index = j
        if index != i :
            swap(index,i)
    return arr
print(selection_sort(arr))