from collections import defaultdict
from typing import List
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)        
        for i, x in enumerate(manager):
            subordinates[x].append(i) 

        def dfs(node):
            time = 0
            for nei in subordinates[node]:
                time = max(dfs(nei), time)
            return time + informTime[node]
        return dfs(headID)
