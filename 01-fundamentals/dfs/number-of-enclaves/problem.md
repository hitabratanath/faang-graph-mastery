# Number of Enclaves

**Difficulty:** Medium
**LeetCode Link:** [Problem 1020](https://leetcode.com/problems/number-of-enclaves/)

## Description
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

## Visual Representation

```
Input grid:
[[0,0,0,0],
 [1,0,1,0],
 [0,1,1,0],
 [0,0,0,0]]

Visualization:
. . . .
X . X .     <- X at (1,0) and (1,2) touch boundary
. X X .     <- X's at (2,1) and (2,2) are enclosed
. . . .

Step-by-step:
1. Border land cells:
   . . . .
   B . B .     (B = border-connected land)
   . . . .
   . . . .

2. Enclosed land (enclaves):
   . . . .
   . . . .
   . E E .     (E = enclave, cannot reach border)
   . . . .

Answer: 2 (cells at [2,1] and [2,2])

Another example:
[[0,1,1,0],
 [0,0,1,0],
 [0,0,1,0],
 [0,0,0,0]]

. X X .
. . X .     <- All X's connected to border
. . X .
. . . .

Answer: 0 (no enclaves, all land reaches boundary)
```

## Examples

**Example 1:**
```
Input: grid = [[0,0,0,0],
               [1,0,1,0],
               [0,1,1,0],
               [0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed
because its on the boundary.
```

**Example 2:**
```
Input: grid = [[0,1,1,0],
               [0,0,1,0],
               [0,0,1,0],
               [0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- grid[i][j] is either 0 or 1
