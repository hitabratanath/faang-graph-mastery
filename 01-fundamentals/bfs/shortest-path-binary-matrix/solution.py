from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1],
            [1, 1], [1, -1], [-1, 1], [-1, -1]
        ]
        queue = deque([(0, 0, 1)])
        visited = set([(0, 0)])

        while queue:
            x, y, dist = queue.popleft()
            if (x, y) == (N - 1, N - 1):
                return dist
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < N and 0 <= ny < N and
                    (nx, ny) not in visited and
                    grid[nx][ny] == 0
                ):
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
        return -1
