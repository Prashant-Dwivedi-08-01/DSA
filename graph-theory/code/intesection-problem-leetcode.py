# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/submissions/

# Below solution is not optimal, Time Limit Exceeded

from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads) -> int:
        g = self.makeAdjList(roads)
        visited = set()
        current_cost = 0
        total_cost_list = []
        self.dfs(0, n-1, visited, current_cost, total_cost_list, g)
        minimum_cost = min(total_cost_list)
        return total_cost_list.count(minimum_cost)
    
    
    def dfs(self, src, dst, visited, current_cost, total_cost_list, g):
        visited.add(src)
        
        if src == dst:
            new_cost = current_cost
            total_cost_list.append(new_cost)
            return total_cost_list
        
        for nb, cost in g[src]:
            if nb not in visited:
                current_cost += cost
                total_cost_list = self.dfs(nb, dst, visited, current_cost, total_cost_list, g)
                current_cost -= cost
                visited.remove(nb)
        return total_cost_list
    
    def makeAdjList(self, roads):
        roads_graph = defaultdict(list)
        for src, dst, cost in roads:
            roads_graph[src].append((dst,cost))
            roads_graph[dst].append((src,cost))
        return roads_graph