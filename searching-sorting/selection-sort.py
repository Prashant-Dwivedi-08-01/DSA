# Here we find the minimum element and place it at first position. 
# Then iterate over the next set of item
# OR we can also find max element and push it to the last

def minIndex(lst):
    return lst.index(min(lst))

def selection_sort(arr):
    for i in range(len(arr)):
        minValueIndex = minIndex(arr[i:]) + i #here we add i as the index is calculated only in remaining part of the array. i.e if we are giving array from index 3 to index 6 then if min ele is at position 2 then index 1 will be returned which is with respect to sliced array

        # place the minimum element at the begin
        temp = arr[i]
        arr[i] = arr[minValueIndex]
        arr[minValueIndex] = temp


arr = [6,1,7,3,5,9,4,2,8,6,3,12,10,4]
selection_sort(arr)
print(arr)
