from collections import defaultdict
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        dist = [float('inf')] * n
        dist[k - 1] = 0

        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        
        # dist, node
        heap = [(0, k - 1)]
        min_time = float('-inf')


        while heap:
            curr_dist, node = heapq.heappop(heap)
            if curr_dist > dist[node]: continue
            
            min_time = max(min_time, curr_dist)
            
            for nei, wt in graph[node]:
                new_wt = curr_dist + wt
                if new_wt < dist[nei]:
                    dist[nei] = new_wt
                    heapq.heappush(heap, (new_wt, nei))
        
        for item in dist:
            if item == float('inf'): return -1
        
        return min_time