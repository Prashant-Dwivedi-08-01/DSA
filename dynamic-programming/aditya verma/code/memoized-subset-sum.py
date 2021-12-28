def subsetSum(integer_array, no_of_integers, target_sum,memo):
    if target_sum == 0:
        return True 
    if no_of_integers <= 0:
        return False

    key = (no_of_integers-1, target_sum)
    if key in memo.keys():
        return memo[key]

    if(integer_array[no_of_integers-1] <= target_sum):
        include_present_integer = integer_array[no_of_integers-1]
        memo[key] = (subsetSum(integer_array, no_of_integers-1, target_sum-include_present_integer, memo) or subsetSum(integer_array, no_of_integers-1, target_sum, memo))
        return memo[key]
       
    elif integer_array[no_of_integers-1] > target_sum:
        memo[key] =  subsetSum(integer_array, no_of_integers-1, target_sum, memo)
        return memo[key]

integer_array = [1,2,3,4,4,5,6,67,12]
no_of_integers = len(integer_array)
target_sum = 9
memo = {}
print(subsetSum(integer_array, no_of_integers, target_sum, memo))