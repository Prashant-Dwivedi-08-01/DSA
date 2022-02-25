def merge_sort_inplace(arr, s, e):
    if e - s == 1 :
        return
    
    mid = (s + e) // 2

    merge_sort_inplace(arr, s, mid)
    merge_sort_inplace(arr, mid, e)

    merge_inplace(arr, s, mid, e)

def merge_inplace(arr, s, mid, e):
    merged_arr = []
    i = s
    j = mid
    while i < mid and j < e:
        if arr[i] > arr[j]:
            merged_arr.append(arr[j])
            j += 1
        else:
            merged_arr.append(arr[i])
            i += 1
    
    while i < mid:
        merged_arr.append(arr[i])
        i += 1
    while j < e:
        merged_arr.append(arr[j])
        j += 1
    
    # replace the contents of the original array
    for i in range(len(merged_arr)):
        arr[s+i] = merged_arr[i]

arr = [0, 5, 4, 6, 3, 2, 1]
merge_sort_inplace(arr,0,len(arr))
print(arr)