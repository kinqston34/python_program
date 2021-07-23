arr = [2,3,45,12,1]
def quick_sort(arr):
    arr = quick_sort_recur(arr,0,len(arr)-1)
    return arr
def quick_sort_recur(arr,first,last):
    if first < last:
        flag = partition(arr,first,last)
        quick_sort_recur(arr,first,flag-1)
        quick_sort_recur(arr,flag+1,last)
    return arr

def partition(arr,first,last):
    def swap(x,y):
        if x != y:
            arr[x],arr[y] = arr[y],arr[x]
    flag = first
    for i in range(first,last):
        if arr[i] <arr[last]: #pivot = last
            swap(flag,i)
            flag += 1
    swap(flag,last)
    return flag
print(quick_sort(arr))