class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(x, y):
            grid2[x][y] = 2
            is_sub = grid1[x][y] == 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid2[nx][ny] == 1:
                    if not dfs(nx, ny): is_sub = False
            return is_sub
        
        sub_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and (i, j):
                    if dfs(i, j):
                        sub_islands += 1
        
        return sub_islands
        