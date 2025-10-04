# Number of Islands

**Difficulty:** Medium
**LeetCode Link:** [Problem 200](https://leetcode.com/problems/number-of-islands/)

## Description
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Visual Representation

```
Grid:
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0

Islands (numbered):
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0

Number of islands: 1 (all 1's are connected)

---

Grid:
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

Islands (numbered):
A A 0 0 0
A A 0 0 0
0 0 B 0 0
0 0 0 C C

Number of islands: 3 (A, B, and C are separate)
```

## Examples

**Example 1:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'
