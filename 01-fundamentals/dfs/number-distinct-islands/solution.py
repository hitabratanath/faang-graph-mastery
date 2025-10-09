from typing import List
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        island_set = set()


        def dfs(x, y, keys, pivot):
            grid[x][y] = 2
            px, py = pivot
            keys.append((x - px, y - py))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    dfs(nx, ny, keys, pivot)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    keys = []
                    pivot = (i, j)
                    dfs(i, j, keys, pivot)
                    island_set.add(tuple(keys))
        
        return len(island_set)