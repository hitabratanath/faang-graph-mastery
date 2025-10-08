'''
cell_to_id[(x, y)] = island_id
id_to_area[island_id] = area
'''
from collections import defaultdict
from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        cell_to_id = defaultdict(int)
        id_to_area = defaultdict(int)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(x, y):
            visited.add((x, y))
            cell_to_id[(x, y)] = island_id
            area = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    area += dfs(nx, ny)
            return area

        area = 0
        island_id = 2
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1 and (i, j) not in visited:
                    id_to_area[island_id] = dfs(i, j)
                    island_id += 1

        max_area = max(id_to_area.values(), default=0)
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    neighbour_id = set()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                            neighbour_id.add(cell_to_id[(nx, ny)])
                    area = 1 + sum([id_to_area[id] for id in neighbour_id])
                    max_area = max(max_area, area)
        return max_area



        
        