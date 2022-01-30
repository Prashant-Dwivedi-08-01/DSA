# 
# *For the Questions with Pattern: 1 to N. This swapping used when numbers are in range.
# *Here, we have only O(n) time Complexity, as the number of Comparisions are 2*N - 1

def cyclic_sort(arr):
    present_index = 0
    while present_index < len(arr):
        correct_index_for_value_at_present_index = arr[present_index] -1
        
        if arr[present_index] == arr[correct_index_for_value_at_present_index]:
            present_index += 1
        else:
            temp = arr[present_index]
            arr[present_index] = arr[correct_index_for_value_at_present_index]
            arr[correct_index_for_value_at_present_index] = temp

arr = [3,5,2,1,4,7,6,-1,-4,23]
cyclic_sort(arr)
print(arr)