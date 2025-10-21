from collections import defaultdict, deque
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        graph = defaultdict(list)
        in_degree = [0] * n

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return result if len(result) == n else []
        