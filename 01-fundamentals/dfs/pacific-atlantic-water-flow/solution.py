from typing import List
class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        pacific_reachable = [[-1] * cols for _ in range(rows)]
        atlantic_reachable = [[-1] * cols for _ in range(rows)]

        def dfs(x, y, ocean):
            ocean[x][y] = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and ocean[nx][ny] == -1 and  grid[nx][ny] >= grid[x][y]:
                    dfs(nx, ny, ocean)

        # top pacific
        for i in range(cols):
            dfs(0, i, pacific_reachable)
        
        # left pacific
        for i in range(rows):
            dfs(i, 0, pacific_reachable)

        # bottom atlantic
        for i in range(cols):
            dfs(rows - 1, i, atlantic_reachable)
        
        for i in range(rows):
            dfs(i, cols - 1, atlantic_reachable)

        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific_reachable[i][j] == 1 and atlantic_reachable[i][j] == 1:
                    result.append([i, j])
        return result