from collections import defaultdict
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        N = len(isConnected)
        visited = set()

        for u in range(N):
            for v in range(N):
                if isConnected[u][v]:
                    graph[u].append(v)

        def dfs(x):
            visited.add(x)
            for nei in graph[x]:
                if nei not in visited:
                    dfs(nei)
        
        count = 0
        for i in range(N):
            if i not in visited:
                count += 1
                dfs(i)
        return count
    

    # or 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(u):
            visited.add(u)
            for i in range(n):
                if isConnected[u][i] and i not in visited:
                    dfs(i)

        count = 0
        for u in range(n):
            if u not in visited:
                count += 1
                dfs(u)
        return count
        
        