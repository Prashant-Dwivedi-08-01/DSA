def subsetSum(integer_array, no_of_integers, target_sum):
    if target_sum == 0:
        return True 
    if no_of_integers <= 0:
        return False

    if(integer_array[no_of_integers-1] <= target_sum):
        include_present_integer = integer_array[no_of_integers-1]
        return (subsetSum(integer_array, no_of_integers-1, target_sum-include_present_integer) or subsetSum(integer_array, no_of_integers-1, target_sum))
        
       
    elif integer_array[no_of_integers-1] > target_sum:
        return subsetSum(integer_array, no_of_integers-1, target_sum)

no_of_integers = 6
integer_array = [3, 34, 4, 12, 5, 2]
target_sum = 9
print(subsetSum(integer_array, no_of_integers, target_sum))