# Minimum Cost to Make at Least One Valid Path (Floyd-Warshall Approach)

**Difficulty:** Hard
**LeetCode Link:** [Problem 1368](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

## Description
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
- 1 which means go to the cell to the right
- 2 which means go to the cell to the left
- 3 which means go to the lower cell
- 4 which means go to the upper cell

Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

## Visual Representation

```
Grid with directions:
[1, 1, 1, 1]  →  →  →  →
[2, 2, 2, 2]  ←  ←  ←  ←
[1, 1, 1, 1]  →  →  →  →
[2, 2, 2, 2]  ←  ←  ←  ←

Direction codes:
1 = RIGHT (→)
2 = LEFT (←)
3 = DOWN (↓)
4 = UP (↑)

Cost = 0: Follow existing arrows
Cost = 1: Change one arrow's direction

Example path with cost 3:
(0,0) → (0,1) → (0,2) → (0,3)
                         ↓ (change: cost +1)
                        (1,3)
                         ↓ (change: cost +1)
                        (2,3)
                         ↓ (change: cost +1)
                        (3,3)
Total cost: 3
```

## Examples

**Example 1:**
```
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
```

**Example 2:**
```
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0,0) to (2,2) without modifying any sign.
```

**Example 3:**
```
Input: grid = [[1,2],[4,3]]
Output: 1
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- 1 <= grid[i][j] <= 4

## Algorithm Notes
This problem can be solved with multiple approaches:
- **0-1 BFS (Deque):** Most efficient - O(mn)
- **Dijkstra:** O(mn log(mn)) - good for learning shortest path
- **Floyd-Warshall:** O((mn)³) - overkill for this problem but demonstrates all-pairs concept

Note: While Floyd-Warshall can solve this, it's not the optimal approach. BFS or Dijkstra are preferred.
