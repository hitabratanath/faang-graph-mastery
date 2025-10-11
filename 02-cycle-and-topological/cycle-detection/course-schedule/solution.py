'''
graph -> adjacency list -> to capture neighors with loops -> simplifies the code
[0, 1]
1 -> 0

0 - not visited
1 - visiting
2 - visited

dfs(node: int) -> bool:
dfs => true -> cycle_present => course_completion -> false
'''


from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        node_state = [0] * numCourses

        def dfs(node):
            if node_state[node] == 1: return True

            node_state[node] = 1
            for nei in graph[node]:
                if node_state[nei] != 2:
                    if dfs(nei): return True
            node_state[node] = 2
            return False
        
        for i in range(numCourses):
            if node_state[i] != 2:
                if dfs(i): return False
        return True
        