def bubble_sort(arr):
    for pass_ in range(len(arr)):
        isSwapped = False
        # in each pass we place one element at it's position form right
        for i in range(1,len(arr)-pass_):
            if arr[i-1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                isSwapped = True
        if not isSwapped:
            return


arr = [5,4,3,2,1]
bubble_sort(arr)
print(arr)