
# LeetCode:https://leetcode.com/problems/regions-cut-by-slashes/submissions/

class Solution:
    
    def regionsBySlashes(self, grid) -> int:
        g = self.makeGrid(grid)
        return self.countConnectedComponent(g)
        
    def countConnectedComponent(self, grid):
        r = c = len(grid)
        count = 0
        visited = set()
        for i in range(r):
            for j in range(c):
                if(grid[i][j] == 0):
                    if (i, j) not in visited:
                        count+=1
                        self.dfs(i, j, grid, r, c,visited)

        return count
                    
    def dfs(self, i, j, grid, r, c,visited):
        if(i < 0 or i >= r or j < 0 or j >= c):
            return
        if(grid[i][j] == 1):
            return
        if((i, j) in visited):
            return
        
        visited.add((i,j))
        
        
        self.dfs(i-1, j, grid, r, c,visited)
        self.dfs(i, j-1, grid, r, c,visited)
        self.dfs(i+1, j, grid, r, c,visited)
        self.dfs(i, j+1, grid, r, c,visited)
        
    
    def makeGrid(self, grid):
        n = len(grid) #grid is array of string. Length represents the 'n' of nxn grid
        
        # make the finer grid in which, the one grid of original grid is divided into 9 parts
        g = [[0]*n*3 for i in range(n*3)] #for 2x2 original grid we have 6x6 new grid
        
        #initializing the grid with  1 for slash present
        # 1--> No region
        # 0--> Region
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    g[i*3][j*3 + 2] = g[i*3 + 1 ][j*3 + 1] = g[i*3 + 2][j*3] =  1
                elif grid[i][j] =='\\':
                    g[i*3][j*3] = g[i*3 + 1][j*3 + 1] = g[i*3 + 2][j*3 + 2] =  1
        return g
                    
        
        