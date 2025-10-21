from collections import defaultdict, deque
from typing import List

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for seq in sequences:
            for num in seq:
                if num not in indegree:
                    indegree[num] = 0

        for seq in sequences:
            for i in range(1, len(seq)):
                u, v  = seq[i - 1], seq[i]
                graph[u].append(v)
                indegree[v] += 1

        queue = deque([node for node, indeg in indegree.items() if indeg == 0])
        order = []
        
        while queue:
            if len(queue) > 1: return False
            node = queue.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0: queue.append(nei)

        return order == nums and len(order) == len(nums)
