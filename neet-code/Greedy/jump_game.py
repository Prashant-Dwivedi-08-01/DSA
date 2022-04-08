# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        bool_arr = [False for i in range(n)]
        bool_arr[0] = True
        
        for i in range(n):
            if bool_arr[i]:
                for j in range(1, nums[i] +1):
                    if i + j < n:
                        bool_arr[i + j] = True
                    else:
                        break
            if bool_arr[n-1]:
                return True
        return False

# https://leetcode.com/problems/jump-game-ii/submissions/
class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.solve(nums,0, len(nums), {}, float("inf")) - 1
    
    def solve(self, nums, idx, n, memo, ans):
        if idx == n - 1:
            return 1
        
        if idx in memo.keys():
            return memo[idx]
        
        for i in range(1, nums[idx]+1):
            if idx + i < n:
                ans = min(ans, 1 + self.solve(nums, idx + i, n, memo, ans))
                
        memo[idx] = ans
        return ans
