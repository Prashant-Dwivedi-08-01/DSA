class Solution:
    def allPathsSourceTarget(self, graph):
        g = self.makeAdjList(graph)
        visited = set()
        current_path = []
        total_paths = []
        dst = len(graph)-1
        
        return self.dfs(0, dst, visited, current_path,total_paths, g)
    
    
    #* Very Important to note is that values are passed by reference. And thus,
    #* they keep changing and updating. There is not seperate instance for each 
    #* recursive call, instead each recursive call is given the updated values of same
    #* instance.
    #* Take example of visited array that we take and keep updating.
    def dfs(self,src, dst, visited, current_path,total_paths, g):
        current_path.append(src)
        if src == dst:
            #* Very important to note is that current_path keeps on changing
            #* If we pass the current path here then, when current path array
            #* changes in future then that current path also changes inside the 
            #* total paths array. Thus you see all the entries in total paths
            #* are same at the end, because every instance we have added in toat paths
            #* have updated to latest one.
            #* Thus, we are adding a copy of current value of current_path list.
            new_path = current_path.copy()
            total_paths.append(current_path)
            return total_paths
        
        for neighbour in g[src]:
            total_paths = self.dfs(neighbour, dst, visited, current_path,total_paths, g)
            current_path.remove(neighbour)
                
        
        return total_paths
    
    def makeAdjList(self, graph):
        g = {}
        for index, list_of_nodes in enumerate(graph):
            g[index] = list_of_nodes
        return g