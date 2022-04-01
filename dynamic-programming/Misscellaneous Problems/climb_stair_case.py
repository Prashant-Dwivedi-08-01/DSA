# https://leetcode.com/problems/climbing-stairs/submissions/

#! Iterative DP
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(46)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

#! Recursive DP
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.solve(0, n, memo)
    
    def solve(self, pres, n, memo):
        if pres == n:
            return 1
        if pres > n:
            return 0
        
        if pres in memo.keys():
            return memo[pres]
        
        memo[pres] = self.solve(pres + 1, n, memo) + self.solve(pres + 2, n, memo)
        return memo[pres]