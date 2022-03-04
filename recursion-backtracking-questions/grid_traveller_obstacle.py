# https://leetcode.com/problems/unique-paths-ii/submissions/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.solve(obstacleGrid, m, n, m, n, {})
    
    def solve(self, grid, m, n, r, c, memo):
        #* The order of these if checks should be same as shown below. Do not change it!
        if m == 0 or n == 0:
            return 0

        if grid[r-m][c-n] == 1:
            return 0

        if m == 1 and n == 1:
            return 1
        
        
        key = (m, n, grid[r-m][c-n])
        if key in memo.keys():
            return memo[key]

        ans = self.solve(grid, m-1, n ,r, c, memo) + self.solve(grid, m , n-1, r, c, memo)
        memo[key] = ans
        return ans

obj = Solution()
obstacleGrid = [[0,1],[0,0]]
print(obj.uniquePathsWithObstacles(obstacleGrid))