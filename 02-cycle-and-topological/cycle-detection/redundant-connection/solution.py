from collections import defaultdict
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(u, target, visited):
            if u == target:
                return True
            visited.add(u)
            for nei in graph[u]:
                if nei not in visited and dfs(nei, target, visited):
                    return True
            return False

        for u, v in edges:
            if u in graph and v in graph and dfs(u, v, set()):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        