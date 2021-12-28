
#* DO NOT WORK ALWAYS

def countSubsetSum(self, nums, n, target_sum, count, memo):
    if target_sum == 0:
        count += 1
        return count
    if n <= 0:
        return count
    #todo: CHECK WHY MEMO IS NOT WORKING 
    # memo
    key = (n-1, target_sum)
    if key in memo.keys():
        return memo[key]
    
    if nums[n-1] <= target_sum:
        count =  self.helper(nums, n-1, target_sum-nums[n-1], count, memo)  
        count = self.helper(nums, n-1, target_sum, count, memo)
        memo[key] = count
        return memo[key]
    else:
        count =  self.helper(nums, n-1, target_sum, count, memo)
        memo[key] = count
        return memo[key]


array = [1,1,1,1,1]
countSubsetSum(array, len(array), 3, 0, {})