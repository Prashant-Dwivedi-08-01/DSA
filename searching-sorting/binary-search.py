def binary_search(arr, target):
    s = 0
    e = len(arr)-1
    while(s <= e):
        mid = s + (e-s)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return -1

arr = [1,2,5,7,8,10]
idx = binary_search(arr, 10)
print(idx)
