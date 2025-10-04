# Number of Distinct Islands

**Difficulty:** Medium
**LeetCode Link:** [Problem 711](https://leetcode.com/problems/number-of-distinct-islands/)

## Description
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (not rotated or reflected) to equal the other.

Return the number of distinct islands.

**Note:** This is a LeetCode Premium problem.

## Visual Representation

```
Grid:
1 1 0 0 0
1 1 0 0 0
0 0 0 1 1
0 0 0 1 1

Island shapes (with their patterns):
Island 1 (top-left):    Island 2 (bottom-right):
  1 1                     1 1
  1 1                     1 1

Pattern: "DRU" (Down, Right, Up from start)
Both islands have the SAME shape!
Number of distinct islands: 1

---

Grid:
1 1 0 1 1
1 0 0 0 0
0 0 0 0 1
1 1 0 1 0

Island 1:     Island 2:     Island 3:     Island 4:
  1 1           1 1           1             1 1
  1             (no Down)     (single)      (L-shape)
  (L-shape)                                 1

Number of distinct islands: 4
```

## Examples

**Example 1:**
```
Input: grid = [[1,1,0,0,0],
               [1,1,0,0,0],
               [0,0,0,1,1],
               [0,0,0,1,1]]
Output: 1
Explanation: Both islands have the same shape.
```

**Example 2:**
```
Input: grid = [[1,1,0,1,1],
               [1,0,0,0,0],
               [0,0,0,0,1],
               [1,1,0,1,0]]
Output: 3
Explanation: Notice how the islands can have different shapes but be considered the same if they can be translated to match.
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1
