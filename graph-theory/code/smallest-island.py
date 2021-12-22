
class Grid:
    visited = set()
    
    def __init__(self, grid):
        self.G = grid
        self.R = len(grid)-1
        self.C = len(grid[0])-1
    
    def smallest_island(self):
        shortest = self.R*self.C
        for r in range(self.R+1):
            for c in range(self.C+1):
                if(self.G[r][c] == 'W'):
                    continue
                else:
                    if((r,c) not in self.visited):
                        size = self.exploreIsland(r,c)
                        if(size < shortest):
                            shortest = size
        
        # print(self.visited)
        return shortest

    def exploreIsland(self, r, c, size = 0):
        if(r > self.R or r<0 or c > self.C or c<0): return size
        if(self.G[r][c] == 'W'): return size
        if((r,c) in self.visited): return size

        self.visited.add((r,c))
        size += 1
        

        size = self.exploreIsland(r-1,c, size)
        size = self.exploreIsland(r,c-1, size)
        size = self.exploreIsland(r+1,c, size)
        size = self.exploreIsland(r,c+1, size)

        return size
        


grid = [
    ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

g = Grid(grid)

print(g.smallest_island())

