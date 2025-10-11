from collections import defaultdict

class Solution:
    def isCycle(self, V, edges):
        graph = defaultdict(list)
        node_state = [0] * V
        
        for u, v in edges:
            graph[u].append(v)
        
        def dfs(node):
            if node_state[node] == 1: return True
            
            node_state[node] = 1
            for nei in graph[node]:
                if node_state[nei] != 2:
                    if dfs(nei): return True
            node_state[node] = 2
            return False
            
        for node in range(V):
            if node_state[node] != 2:
                if dfs(node): return True
        return False