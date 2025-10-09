from typing import List
class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(x, y):
            grid[x][y] = 'M'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 'O':
                    dfs(nx, ny)

        # top
        for i in range(cols):
            if grid[0][i] == 'O':
                dfs(0, i)
        # bottom
        for i in range(cols):
            if grid[rows - 1][i] == 'O':
                dfs(rows - 1, i)
        # left
        for i in range(rows):
            if grid[i][0] == 'O':
                dfs(i, 0)
        # right
        for i in range(rows):
            if grid[i][cols - 1] == 'O':
                dfs(i, cols - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'M': grid[i][j] = 'O'
                else: grid[i][j] = 'X'