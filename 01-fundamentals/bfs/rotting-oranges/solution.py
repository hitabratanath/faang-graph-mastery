class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = 0
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh_oranges = 0

        # collecting all the rotten cells
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j)) 
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        while queue and fresh_oranges:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        queue.append((nx, ny))
            time += 1

        return time if fresh_oranges == 0 else -1      