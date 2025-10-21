class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        state = [0] * n
        res = []

        def dfs(node):
            if state[node] == 1: return False
            if state[node] == 2: return True
            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei): return False
            state[node] = 2
            return True

        for i in range(n):
            if dfs(i): res.append(i)
        return res
