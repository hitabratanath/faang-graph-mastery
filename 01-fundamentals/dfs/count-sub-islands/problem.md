# Count Sub Islands

**Difficulty:** Medium
**LeetCode Link:** [Problem 1905](https://leetcode.com/problems/count-sub-islands/)

## Description
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

## Visual Representation

```
grid1:                    grid2:
[[1,1,1,0,0],            [[1,1,1,0,0],
 [0,1,1,1,1],             [0,0,1,1,1],
 [0,0,0,0,0],             [0,1,0,0,0],
 [1,1,0,0,1],             [1,0,1,1,0],
 [1,0,1,0,1]]             [0,1,0,1,0]]

Analysis:
Island 1 in grid2 (top):
X X X . .
. . X X X    <- All cells also exist in grid1? YES (sub-island)
. . . . .
. . . . .
. . . . .

Island 2 in grid2 (middle-left):
. . . . .
. . . . .
. X . . .    <- Cell (2,1) is not in grid1? NO (not a sub-island)
X . . . .
. . . . .

Island 3 in grid2 (middle-right):
. . . . .
. . . . .
. . . . .
. . X X .    <- All cells also exist in grid1? YES (sub-island)
. . . . .

Island 4 in grid2 (scattered):
. . . . .
. . . . .
. . . . .
. . . . .
. X . X .    <- All cells also exist in grid1? YES (sub-island)

Answer: 3 sub-islands

Overlay visualization:
grid2 cell is sub-island if:
- It's land (1) in grid2, AND
- It's also land (1) in grid1 at same position
```

## Examples

**Example 1:**
```
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,1,0,0,1],[1,0,1,0,1]],
       grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
```

**Example 2:**
```
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
       grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
```

## Constraints
- m == grid1.length == grid2.length
- n == grid1[i].length == grid2[i].length
- 1 <= m, n <= 500
- grid1[i][j] and grid2[i][j] are either 0 or 1
