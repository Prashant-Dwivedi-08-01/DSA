from queue import PriorityQueue
from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.G = defaultdict(list)

    def addEdge(self, source, destination, edgeCost):
        self.G[source].append((destination, edgeCost))

    def printGraph(self):
        print(self.G[0])
        print(self.G[1])
        print(self.G[2])
        print(self.G[3])
        print(self.G[4])
    
    def dijkstra(self,start):
        n = self.V
        vistedNode = [False]*n
        distance = [float('inf')]*n
        distance[0] = 0
        q = PriorityQueue()
        q.put((0,int(start))) #! here we are using (value, index ) and not the (index, value) as discussed in algorithm
        i = 1
        while(not q.empty()):
            print(f'Iteration: {i}')
            i+=1
            minValue, index = q.get()
            if(distance[index] < minValue):continue #! If present distance is already less then no need to reassess this node. Look Algorith for better understanding
            vistedNode[index] = True
            for neighbour in self.G[index]:
                node,cost = neighbour
                if(vistedNode[node]):
                    continue
                newDistanceToThisNode = distance[index] + cost
                if(newDistanceToThisNode < distance[node]):
                    distance[node] = newDistanceToThisNode
                    q.put((newDistanceToThisNode, node))
        return distance


g = Graph(5)
g.addEdge(0,1,4)
g.addEdge(0,2,1)
g.addEdge(1,3,1)
g.addEdge(2,1,2)
g.addEdge(2,3,5)
g.addEdge(3,4,3)


distance = g.dijkstra(0)
print(distance)



