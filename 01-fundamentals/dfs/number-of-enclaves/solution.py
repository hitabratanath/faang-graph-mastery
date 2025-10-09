from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        count = 0


        def dfs(x, y):
            grid[x][y] = 2
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    dfs(nx, ny)

        for j in range(cols):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[rows - 1][j] == 1:
                dfs(rows - 1, j)

        for i in range(rows):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][cols - 1] == 1:
                dfs(i, cols - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
        return count