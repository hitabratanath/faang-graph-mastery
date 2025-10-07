from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = [[-1] * cols for _ in range(rows)]
        queue = deque()
        max_dist = -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    result[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and result[nx][ny] == -1:
                    result[nx][ny] = result[x][y] + 1
                    max_dist = max(max_dist, result[nx][ny])
                    queue.append((nx, ny))
        
        return max_dist