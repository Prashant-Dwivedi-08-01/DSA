#
#* Look at the image in adityaverma/images

def helper(array, memo, n, array_sum, current_sum):
    if(n <= 0):
        return abs(current_sum - (array_sum-current_sum))
    

    key = (n-1, current_sum)
    if key in memo.keys():
        return memo[key]

    memo[key] = min(helper(array, memo, n-1, array_sum, current_sum+array[n-1]) , helper(array, memo, n-1, array_sum, current_sum))
    return memo[key]


array = [1,2,7]
memo = {}
array_sum = sum(array)

print(helper(array, memo, len(array), array_sum, 0))
print(memo)