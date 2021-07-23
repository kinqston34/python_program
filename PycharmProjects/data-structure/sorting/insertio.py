arr = [2,3,45,12,1]
def insertion_sort(arr):
    def swap(a,b):
        arr[a],arr[b] = arr[b],arr[a]

    for i in range(len(arr)):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            swap(j,j-1)
            j -= 1
    return arr
print(insertion_sort(arr))