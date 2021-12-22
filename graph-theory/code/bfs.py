from queue import Queue

graph = {
     'A': ['B', 'F'],
     'B': ['C', 'D'],
     'C': ['E'],
     'D': [],
     'E': [],
     'F': []
    }
visited = {
     'A': False,
     'B': False,
     'C': False,
     'D': False,
     'E': False,
     'F': False,
    }

path = []

def bfs(start,graph):
    q = Queue()
    q.put(start)
    
    while(not q.empty()):
        presentNode = q.get()
        path.append(presentNode) # or print(presentNode)
        neighbours = graph[presentNode]
        for neighbour in neighbours:
            if(not visited[neighbour]):
                q.put(neighbour)
                visited[neighbour] = True

bfs('A',graph)
for x in path:
    print(x)



