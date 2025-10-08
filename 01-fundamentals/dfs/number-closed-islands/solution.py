from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(x, y):
            if not (0 <= x < rows and 0 <= y < cols):
                return False
            if grid[x][y] == 1 or grid[x][y] == 2: return True

            grid[x][y] = 2
            surrounded = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not dfs(nx, ny): surrounded =  False
            return surrounded
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1
        return count 
        