from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        source, destination = (0, 0), (rows - 1, cols - 1)
        result = [[float('inf')] * cols for _ in range(rows)]
        result[0][0] = grid[0][0]
        heap = [(grid[0][0], (0, 0))]

        while heap:
            time, cell = heapq.heappop(heap)
            if cell == destination: return time

            x, y = cell
            if result[x][y] < time: continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_time = max(time, grid[nx][ny])
                    if new_time < result[nx][ny]:
                        result[nx][ny] = new_time
                        heapq.heappush(heap, (new_time, (nx, ny)))

        