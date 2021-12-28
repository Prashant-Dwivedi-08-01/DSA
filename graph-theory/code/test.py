def subsetSum(integer_array, no_of_integers, target_sum,memo):
    if target_sum == 0:
        return True 
    if no_of_integers <= 0:
        return False

    if integer_array[no_of_integers-1] in memo.keys():
            return memo[integer_array[no_of_integers-1]]

    if(integer_array[no_of_integers-1] <= target_sum):
        include_present_integer = integer_array[no_of_integers-1]
        memo[integer_array[no_of_integers-1]] = (subsetSum(integer_array, no_of_integers-1, target_sum-include_present_integer, memo) or subsetSum(integer_array, no_of_integers-1, target_sum, memo))
        return memo[integer_array[no_of_integers-1]]
       
    elif integer_array[no_of_integers-1] > target_sum:
        memo[integer_array[no_of_integers-1]] =  subsetSum(integer_array, no_of_integers-1, target_sum, memo)
        return memo[integer_array[no_of_integers-1]]

no_of_integers = 5
# integer_array = [14,9,8,4,3,2]
integer_array = [2,3,4,8,9,14]
target_sum = 20
print(subsetSum(integer_array, no_of_integers, target_sum, {}))