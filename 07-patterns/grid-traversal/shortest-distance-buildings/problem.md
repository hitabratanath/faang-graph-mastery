# Shortest Distance from All Buildings

**Difficulty:** Hard
**LeetCode Link:** [Problem 317](https://leetcode.com/problems/shortest-distance-from-all-buildings/)

## Description
You are given an m x n grid grid of values 0, 1, or 2, where:
- Each 0 marks an empty land that you can pass by freely
- Each 1 marks a building that you cannot pass through
- Each 2 marks an obstacle that you cannot pass through

You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

**Note:** This is a LeetCode Premium problem.

## Visual Representation

```
Grid (0 = empty, 1 = building, 2 = obstacle):
1 0 2 0 1
0 0 0 0 0
0 0 1 0 0

Distance calculation from position (1,2):
To building at (0,0): |0-1| + |0-2| = 3
To building at (0,4): |0-1| + |4-2| = 3
To building at (2,2): |2-1| + |2-2| = 1
Total distance: 3 + 3 + 1 = 7

Distance map for all empty cells:
  1 7 2 8 1
  6 5 4 5 6
  7 6 1 6 7

Minimum total distance: 7 (at position (1,2))
```

## Examples

**Example 1:**
```
Input: grid = [[1,0,2,0,1],
               [0,0,0,0,0],
               [0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance
of 3+3+1=7 is minimal. So return 7.
```

**Example 2:**
```
Input: grid = [[1,0]]
Output: 1
```

**Example 3:**
```
Input: grid = [[1]]
Output: -1
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0, 1, or 2
- There will be at least one building in the grid
