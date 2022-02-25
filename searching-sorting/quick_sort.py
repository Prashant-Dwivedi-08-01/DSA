def quick_sort(arr, left, right):
    if right <= left:
        return
    
    s = left
    e = right
    mid = s + (e-s)//2
    pivot = arr[mid] # position of pivot is moving in the arr thus dont make use of arr[mid]
    while s <= e:
        while arr[s] < pivot:
            s += 1
        while arr[e] > pivot:
            e -= 1
        if s <= e:
            temp = arr[e]
            arr[e] = arr[s]
            arr[s] = temp
            s += 1
            e -= 1
    quick_sort(arr, left, e)
    quick_sort(arr, s, right)

arr = [9,6,8,9,2,3,5,7,3]
quick_sort(arr, 0, len(arr)-1)
print(arr)