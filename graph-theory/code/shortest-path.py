from collections import defaultdict
from queue import Queue

class Graph:

    visited = set()
    
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

    #! This would be simple bfs with count of distance at each node,
    #! and then returning the moment we found the first occurence of the node.
    #! Here, instead using dfs, we use bfs, as bfs ensures that the moment we get 
    #! the first node then it will be the shortest distance to it from source. One can 
    #! Confirm this by drawing a graph

    def shortest_path(self, src, dst): 
        q = Queue()
        q.put((src,0))
        while(not q.empty()):
            currentNode, dist = q.get()
            self.visited.add(currentNode)
            for neighbour in self.G[currentNode]:
                if neighbour not in self.visited:
                    if( neighbour == dst):
                        return dist+1
                    q.put((neighbour, dist+1))
        return -1


edges = [
 ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

g = Graph(edges)

g.printGraph()

print(g.shortest_path('b','g'))
