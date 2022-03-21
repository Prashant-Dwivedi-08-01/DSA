#
#* In this approach we are spending more memory in maintaing the count variable. 
#* And this variable is also filled in the stack

def helper(nums, n, target_sum, count, memo):
    if target_sum == 0:
        count += 1
        return count
    if n <= 0:
        return count
    #todo: CHECK WHY MEMO IS NOT WORKING 
    # memo
    key = (n-1, target_sum, count) #* Include all the changing variables in making the key
    if key in memo.keys():
        return memo[key]
    
    if nums[n-1] <= target_sum:
        count =  helper(nums, n-1, target_sum-nums[n-1], count, memo)  
        count = helper(nums, n-1, target_sum, count, memo)
        memo[key] = count
        return memo[key]
    else:
        count =  helper(nums, n-1, target_sum, count, memo)
        memo[key] = count
        return memo[key]


array = [1,1,1,1,1]
print(helper(array, len(array), 3, 0, {}))