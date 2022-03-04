# https://leetcode.com/problems/unique-paths-iii/submissions/
class Solution:
    def uniquePathsIII(self, grid) -> int:
        r = len(grid)
        c = len(grid[0])
        total_possible = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] != -1:
                    total_possible += 1
                if grid[i][j] == 1:
                    m = r-i
                    n = c-j
        visited = [(m,n)]
        all_paths = self.solve(grid, m, n, r, c, [],total_possible, visited, {})
        print(all_paths)
        return all_paths
    
    def solve(self, grid, m, n, r, c, present_path,total_possible, visited, memo):
        if m == 0 or n == 0 or m > r or n > c:
            return []
        
        if grid[r-m][c-n] == 2:
            new_array = []
            present_path.append((r-m, c-n))
            if len(present_path) == total_possible:
                new_array.append(present_path.copy())
            present_path.pop()
            return new_array
        
        if grid[r-m][c-n] == -1:
            return []
        
        present_path.append((r-m, c-n))
        new_array = []
        if (m+1, n) not in visited:
            visited.append((m+1, n))
            new_array.extend(self.solve(grid, m+1, n, r, c, present_path,total_possible, visited, memo))
            visited.pop()
        if (m-1, n) not in visited:
            visited.append((m-1, n))
            new_array.extend(self.solve(grid, m-1, n, r, c, present_path,total_possible, visited, memo))
            visited.pop()
        if (m, n+1) not in visited:
            visited.append((m, n+1))
            new_array.extend(self.solve(grid, m, n+1, r, c, present_path,total_possible, visited, memo))
            visited.pop()
        if (m, n-1) not in visited:
            visited.append((m, n-1))
            new_array.extend(self.solve(grid, m, n-1, r, c, present_path,total_possible, visited, memo))
            visited.pop()
        present_path.pop()
        return new_array

grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
obj = Solution()
print(len(obj.uniquePathsIII(grid)))