from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        in_order = [0] *  n
        for u, v in edges:
            in_order[v - 1] += 1
            in_order[u - 1] += 1
            if in_order[v - 1] == n - 1: return v
            if in_order[u - 1] == n - 1: return u