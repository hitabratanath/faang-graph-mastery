from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inorder = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            inorder[u] += 1
            inorder[v] += 1
        
        queue = deque([i for i in range(n) if inorder[i] == 1])
        remaining = n

        while remaining > 2:
            remaining -= len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                for nei in graph[node]:
                    inorder[nei] -= 1
                    if inorder[nei] == 1:
                        queue.append(nei)
        
        return list(queue)

        