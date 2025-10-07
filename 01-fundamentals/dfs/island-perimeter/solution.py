class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def getPeri(x, y):
            peri = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] == 0:
                    peri += 1
            return peri
            
        
        def dfs(x, y):
            grid[x][y] = 2
            perimeter = getPeri(x, y)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    perimeter += dfs(nx, ny)
            return perimeter
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0