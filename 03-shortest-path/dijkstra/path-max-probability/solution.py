from collections import defaultdict
from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        prob = [0] * n
        prob[start_node] = 1

        # maxHeap
        # (-prop, node)
        heap = [(-1, start_node)]
        
        while heap:
            p, node = heapq.heappop(heap)
            if node == end_node:
                return -p
            if -p < prob[node]: continue
            
            for nei, pr in graph[node]:
                new_pr = pr * -p
                if new_pr > prob[nei]:
                    prob[nei] = new_pr
                    heapq.heappush(heap, (-new_pr, nei))
        return 0