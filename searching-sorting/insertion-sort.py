def insertion_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, 0,-1):
            if arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else:
                break # rest of the elements to the left are definitely smaller than this

arr = [5,4,3,2,1]
insertion_sort(arr)
print(arr)