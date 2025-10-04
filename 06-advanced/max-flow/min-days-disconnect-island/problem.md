# Minimum Number of Days to Disconnect Island

**Difficulty:** Hard
**LeetCode Link:** [Problem 1568](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/)

## Description
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

## Visual Representation

```
Example 1: Disconnect Island

Initial Grid:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,0]]

Day 0 (Initial):
    0  1  1  0
    0  1  1  0
    0  0  0  0

One island (all 1's connected)

Day 1 (Remove one cell):
    0  1  1  0
    0  1  0  0  ← Changed (1,2) to 0
    0  0  0  0

Still one island (top 3 cells still connected)

Day 2 (Remove another cell):
    0  1  0  0  ← Changed (0,2) to 0
    0  1  0  0
    0  0  0  0

Two separate islands! (disconnected)
Answer: 2 days


Example 2: Articulation Point

Initial Grid:
[[1,1,0,1,1],
 [1,1,1,1,1],
 [1,1,0,1,1],
 [1,1,0,1,1]]

Visualization with coordinates:
    1  1  0  1  1
    1  1  1  1  1  ← Cell (1,2) is articulation point
    1  1  0  1  1
    1  1  0  1  1

Removing cell (1,2):
    1  1  0  1  1
    1  1  0  1  1  ← Changed to 0
    1  1  0  1  1
    1  1  0  1  1

Result: Two islands (left side and right side separated)
Answer: 1 day


Max-Flow / Min-Cut Perspective:

The problem is related to finding the minimum vertex cut:
- If there's an articulation point: answer = 1
- If the island is a single cell: answer = 1
- If there are only 2 cells: answer = 2
- Otherwise: answer = 2 (can always disconnect by removing 2 cells)

Graph structure:
    A --- B --- C
          |
          D --- E

B is an articulation point (removing B disconnects the graph)


Single chain example (always 2 days):
    A --- B --- C --- D --- E

No single articulation point, need to remove 2 cells
```

## Examples

**Example 1:**
```
Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 separated islands.
```

**Example 2:**
```
Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 30
- grid[i][j] is either 0 or 1
