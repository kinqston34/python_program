arr = [2,3,45,12,1]

def merge_sort(arr):
    def merge(left,right,merged):
        lc,rc = 0,0

        while lc < len(left) and rc < len(right):
            if left[lc] <= right[rc]:
                merged[lc+rc] = left[lc]
                lc += 1
            else:
                merged[lc+rc] = right[rc]
                rc += 1
        print('while,merged:',merged)
        for i in range(lc,len(left)):
            merged[i+rc] = left[i]
        for i in range(lc,len(right)):
            merged[lc+i] = right[i]
        print('for,merged:', merged)
        return merged

    if len(arr) <= 1:
        return arr
    #divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    #conquer
    return merge(left,right,arr.copy())

merge_sort(arr)