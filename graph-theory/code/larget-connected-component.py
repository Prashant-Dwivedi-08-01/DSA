class Graph:
    visited = set() #! here the time complexity to check is O(1) as compared to list where it was O(n)

    def __init__(self, graph):
        self.G = graph
    
    def largest_connected_component(self):
        longest = 0
        for node in self.G.keys():
            if node not in self.visited:
                this_size = self.dfs(node)
                if this_size > longest:
                    longest = this_size
        return longest

    def dfs(self, src, size = 0):
        self.visited.add(src)
        size += 1 # after we append a node in visited that means this must be now counted
        for neighbour in self.G[src]:
            if neighbour not in self.visited:
                size = self.dfs(neighbour, size) #! Understand this diagramatically if not understood
        return size

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

print(g.largest_connected_component())