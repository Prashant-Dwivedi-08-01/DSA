#
#* Look at the image in adityaverma/images. We neede to minimize the difference of two subsets. Thus return should be min of diff of two subset

def helper(array, memo, n, array_sum, current_sum):
    if(n <= 0):
        sum_of_subset_formed_till_now = current_sum
        sum_of_subset_of_remaining_elements = array_sum-current_sum #for eg: I we made a subset of sum 10 then sum of remaining elements would be 5( Assumin total array sum to be 15)
        
        diff_of_current_two_subsets = abs(sum_of_subset_formed_till_now - sum_of_subset_of_remaining_elements) 
        return diff_of_current_two_subsets
    

    key = (n-1, current_sum)
    if key in memo.keys():
        return memo[key]

    memo[key] = min( helper(array, memo, n-1, array_sum, current_sum+array[n-1]) ,\
                     helper(array, memo, n-1, array_sum, current_sum))
    return memo[key]


array = [1,2,7]
memo = {}
array_sum = sum(array)

print(helper(array, memo, len(array), array_sum, 0))
print(memo)