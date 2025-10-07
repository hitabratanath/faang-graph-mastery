from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        result = [[-1] * cols for _ in range(rows)]
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and result[nx][ny] == -1:
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))

        return result 
        
