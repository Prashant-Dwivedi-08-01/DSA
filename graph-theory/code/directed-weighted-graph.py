from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.G = defaultdict(list)

    def addEdge(self, source, destination, edgeCost):
        self.G[source].append((destination, edgeCost))

    def printGraph(self):
        for node in range(0, self.V):
            print(f'{node} --> {self.G[node]}')
    

g = Graph(5)
g.addEdge(0,1,4)
g.addEdge(0,2,1)
g.addEdge(1,3,1)
g.addEdge(2,1,2)
g.addEdge(2,3,5)
g.addEdge(3,4,3)

g.printGraph()


