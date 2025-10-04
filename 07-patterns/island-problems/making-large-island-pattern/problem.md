# Making a Large Island

**Difficulty:** Hard
**LeetCode Link:** [Problem 827](https://leetcode.com/problems/making-a-large-island/)

## Description
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

## Visual Representation

```
Original grid:
1 0
0 1

Option 1: Change (0,1) from 0 to 1:
1 1
0 1
Result: Island size = 3

Option 2: Change (1,0) from 0 to 1:
1 0
1 1
Result: Island size = 3

Maximum island size: 3

---

More complex example:
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

If we change (0,2) from 0 to 1:
1 1 1 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

This connects the top-left island (size 4) with the middle island (size 1).
New island size: 4 + 1 + 1 (the changed cell) = 6
```

## Examples

**Example 1:**
```
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
```

**Example 2:**
```
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
```

**Example 3:**
```
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
```

## Constraints
- n == grid.length
- n == grid[i].length
- 1 <= n <= 500
- grid[i][j] is either 0 or 1
