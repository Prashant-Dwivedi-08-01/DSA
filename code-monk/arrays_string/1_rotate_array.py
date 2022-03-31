
# This solution is of no extra space: https://leetcode.com/problems/rotate-array/
"""
1. Reverse entire array
2. Then reverse upto K
3. Then reverse from k+1 to end
"""
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums) - 1)
        
    
    def reverse(self, lst, start, end):
        while start < end:
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp
            start += 1
            end -= 1