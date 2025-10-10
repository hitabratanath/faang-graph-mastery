from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_order = [0] * n
        out_order = [0] * n
        for u, v in trust:
            in_order[v - 1] += 1
            out_order[u - 1] += 1
        
        potential_judges = []
        for i in range(n):
            if not out_order[i]:
                potential_judges.append(i)
        
        for i in potential_judges:
            if in_order[i] == n - 1:
                return i + 1
        return -1

        