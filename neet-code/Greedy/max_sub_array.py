# https://leetcode.com/problems/jump-game/
from typing import List

#* This is also known as Kaden's Algo. Look Images

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        maxSubArray = nums[0]
        
        for n in nums:
            # check prefix first
            if prefix < 0:
                prefix = 0
            prefix += n
            maxSubArray = max(maxSubArray, prefix)
        return maxSubArray