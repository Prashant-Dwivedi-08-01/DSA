def countSubsetSum(nums, n, target_sum, memo):
    if target_sum == 0:
        return 1
    if n <= 0:
        return 0
    #todo: CHECK WHY MEMO IS NOT WORKING 
    # memo
    key = (n-1, target_sum)
    if key in memo.keys():
        return memo[key]
    
    if nums[n-1] <= target_sum:
        memo[key] =  countSubsetSum(nums, n-1, target_sum-nums[n-1], memo) + countSubsetSum(nums, n-1, target_sum, memo)
        return memo[key]
    else:
        memo[key] =  countSubsetSum(nums, n-1, target_sum,memo)
        return memo[key]



array = [1,2,3,4,4,5,6,67,12]
print(countSubsetSum(array, len(array), 9, {}))