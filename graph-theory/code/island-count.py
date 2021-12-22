
class Grid:
    visited = set()
    
    def __init__(self, grid):
        self.G = grid
        self.R = len(grid)-1
        self.C = len(grid[0])-1
        # print(len(grid)-1)
        # print(len(grid[0])-1)
    
    def island_count(self):
        count = 0
        for r in range(self.R+1):
            for c in range(self.C+1):
                if(self.G[r][c] == 'W'):
                    continue
                else:
                    if((r,c) not in self.visited):
                        count+=1
                        self.exploreIsland(r,c)
        
        # print(self.visited)
        return count

    def exploreIsland(self, r, c):
        if(r > self.R or r<0 or c > self.C or c<0): return 
        if(self.G[r][c] == 'W'): return
        if((r,c) in self.visited): return

        self.visited.add((r,c))
        

        self.exploreIsland(r-1,c)
        self.exploreIsland(r,c-1)
        self.exploreIsland(r+1,c)
        self.exploreIsland(r,c+1)
        


grid = [
 ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

g = Grid(grid)

print(g.island_count())