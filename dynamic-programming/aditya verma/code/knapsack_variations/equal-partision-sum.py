class Solution:
    def canPartition(self, nums) -> bool:
        presentSum = sum(nums)
        print(presentSum)
        if(presentSum & 1):
            return False
        else:
            memo = {}
            return self.subsetSum(nums, len(nums), presentSum//2, memo)
    
    def subsetSum(self, integer_array, no_of_integers, target_sum,memo):
        if target_sum == 0:
            return True 
        if no_of_integers <= 0:
            return False

        key = (no_of_integers-1, target_sum)
        if key in memo.keys():
            return memo[key]

        if(integer_array[no_of_integers-1] <= target_sum):
            include_present_integer = integer_array[no_of_integers-1]
            memo[key] = (self.subsetSum(integer_array, no_of_integers-1, target_sum-include_present_integer, memo) or self.subsetSum(integer_array, no_of_integers-1, target_sum, memo))
            return memo[key]
        
        elif integer_array[no_of_integers-1] > target_sum:
            memo[key] =  self.subsetSum(integer_array, no_of_integers-1, target_sum, memo)
            return memo[key]


obj = Solution()
array = [23,13,11,7,6,5,5]
print(obj.canPartition(array))