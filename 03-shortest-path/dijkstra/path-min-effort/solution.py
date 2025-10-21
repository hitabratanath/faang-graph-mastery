from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        source, destination = (0, 0), (rows - 1, cols - 1)
        result = [[float('inf')] * cols for _ in range(rows)]
        result[0][0] = 0
        heap = [(0, source)]

        while heap:
            dist, cell = heapq.heappop(heap)
            if cell == destination: return dist
            x, y = cell
            if result[x][y] < dist: continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_dist = max(dist, abs(heights[nx][ny] - heights[x][y]))
                    if new_dist < result[nx][ny]:
                        result[nx][ny] = new_dist
                        heapq.heappush(heap, (new_dist, (nx, ny)))
        return -1

        