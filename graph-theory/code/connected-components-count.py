
class Graph:
    visited = set()#! here the time complexity to check is O(1) as compared to list where it was O(n)
    def __init__(self, graph):
        self.G = graph
    
    def connected_components_count(self):
        count = 0
        for node in self.G.keys():
            if node not in self.visited:
                self.dfs(node)
                count+=1
        return count
    
    def dfs(self, src):
        self.visited.add(src)
        for neighbour in self.G[src]:
            if(neighbour not in self.visited):
                self.dfs(neighbour)

graph = {
 0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}

g = Graph(graph)

print(g.connected_components_count())