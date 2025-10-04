# Number of Closed Islands

**Difficulty:** Medium
**LeetCode Link:** [Problem 1254](https://leetcode.com/problems/number-of-closed-islands/)

## Description
Given a 2D grid consists of 0s (land) and 1s (water). An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

## Visual Representation

```
Input grid:
[[1,1,1,1,1,1,1,0],
 [1,0,0,0,0,1,1,0],
 [1,0,1,0,1,1,1,0],
 [1,0,0,0,0,1,0,1],
 [1,1,1,1,1,1,1,0]]

Visualization (. = land/0, # = water/1):
# # # # # # # .
# . . . . # # .
# . # . # # # .
# . . . . # . #
# # # # # # # .

Islands analysis:
1. Left island (row 1-3, col 1-4):
   # # # # # # # .
   # X X X X # # .  <- Closed island (surrounded by #)
   # X # X # # # .
   # X X X X # . #
   # # # # # # # .

2. Right column (col 7):
   # # # # # # # .
   # . . . . # # .  <- Not closed (touches border)
   # . # . # # # .
   # . . . . # . #
   # # # # # # # .

Answer: 2 closed islands

Another example:
[[0,0,1,0,0],
 [0,1,0,1,0],
 [0,1,1,1,0]]

. . # . .
. # . # .    <- No closed islands (all land touches border)
. # # # .

Answer: 1 (center island at [1,2])
```

## Examples

**Example 1:**
```
Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]
Output: 2
Explanation: Islands in grey are closed because they are completely surrounded by water (group of 1s).
```

**Example 2:**
```
Input: grid = [[0,0,1,0,0],
               [0,1,0,1,0],
               [0,1,1,1,0]]
Output: 1
```

**Example 3:**
```
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
```

## Constraints
- 1 <= grid.length, grid[0].length <= 100
- 0 <= grid[i][j] <= 1
