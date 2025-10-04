# Number of Closed Islands

**Difficulty:** Medium
**LeetCode Link:** [Problem 1254](https://leetcode.com/problems/number-of-closed-islands/)

## Description
Given a 2D grid consists of 0s (land) and 1s (water). An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

## Visual Representation

```
Grid (0 = land, 1 = water):
1 1 1 1 1 1 1 0
1 0 0 0 0 1 1 0
1 0 1 0 1 1 1 0
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 0

Islands analysis:
- Top-right island: NOT closed (touches edge)
- Left island: CLOSED (surrounded by 1s)
- Bottom-right island: NOT closed (touches edge)

Number of closed islands: 2

Visual with marked closed islands (C):
1 1 1 1 1 1 1 0
1 C C C C 1 1 0
1 C 1 C 1 1 1 0
1 C C C C 1 0 1
1 1 1 1 1 1 1 0
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
