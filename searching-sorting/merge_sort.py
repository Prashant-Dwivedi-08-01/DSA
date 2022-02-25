def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[:mid].copy())
    right = merge_sort(arr[mid:].copy())

    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    merged_arr = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged_arr.append(right[j])
            j += 1
        else:
            merged_arr.append(left[i])
            i += 1
    while i < len(left):
        merged_arr.append(left[i])
        i += 1
    while j < len(right):
        merged_arr.append(right[j])
        j += 1
    
    return merged_arr
    
arr = [0, 5, 4, 6, 3, 2, 1]
arr = merge_sort(arr)
print(arr)