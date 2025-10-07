from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(x, y):
            if (x, y) in visited:
                return
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 0:
                        queue.append((x, y))
                    else:
                        dfs(nx, ny)

        # mark first island and add boundary zeros to queue
        found = False
        for i in range(rows):
            if found: break
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # BFS to reach second island
        distance = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if not (0<=nx<rows and 0<=ny<cols) or (nx, ny) in visited:
                        continue
                    if grid[nx][ny] == 1:
                        return distance
                    queue.append((nx, ny))
                    visited.add((nx, ny))
            distance += 1

        return distance
