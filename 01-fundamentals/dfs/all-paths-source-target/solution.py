class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = [] 
        target = len(graph) - 1

        def dfs(node, path):
            if node == target:
                result.append(path)
                return
            
            for nei in graph[node]:
                dfs(nei, path + [nei])
                
        dfs(0, [0])
        return result
        