from collections import defaultdict

#* hasPath() problem using dfs() approach

class Graph:
    def __init__(self, v):
        self.V = v
        self.G = defaultdict(list)
    
    def addEdge(self, src, dst):
        self.G[src].append(dst)

    def printGraph(self):
        for key,value in self.G.items():
            print(f'{key} -> {value}')
    
    def hasPath(self, src, dst):
        if(src == dst):
            return True
        
        for neighbour in self.G[src]:
            if(self.hasPath(neighbour, dst)):
                return True #! early return if any Path is found.Run for all the neighbours if early returndoest not happen, viz. basic dfs
        return False

g = Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)

print(g.printGraph())
# print(g.hasPath(2,4))