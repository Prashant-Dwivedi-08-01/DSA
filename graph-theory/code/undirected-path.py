
from collections import defaultdict

#* hasPath() problem using dfs() approach

class Graph:
    def __init__(self, edges):
        self.G = self.adj_list(edges)
    
    def adj_list(self, edges):
        g = defaultdict(list)
        for (src,dst) in edges:
            g[src].append(dst)
            g[dst].append(src)
        return g


    def printGraph(self):
        for key,value in self.G.items():
            print(f'{key} -> {value}')
    
    def hasPath(self, src, dst, visited = []):
        if(src == dst):
            return True
        
        visited.append(src)
        for neighbour in self.G[src]:
            if(neighbour not in visited):
                if(self.hasPath(neighbour, dst, visited)):
                    return True #! early return if any Path is found.Run for all the neighbours if early returndoest not happen, viz. basic dfs
        return False



# here we have the edge list 
edges = [
  ('i','j'),
  ('k','i'),
  ('m','k'),
  ('k','l'),
  ('o','n')
]
g = Graph(edges)

g.printGraph()

print("Has Path: ", g.hasPath('k','n'))