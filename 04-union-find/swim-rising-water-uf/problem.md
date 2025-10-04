# Swim in Rising Water

**Difficulty:** Hard
**LeetCode Link:** [Problem 778](https://leetcode.com/problems/swim-in-rising-water/)

## Description
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

## Visual Representation

```
Example: grid = [[0,2],[1,3]]

Grid visualization:
  0  2
  1  3

Path from (0,0) to (1,1):

Time t=0: Can only be at elevation ≤ 0
  [X][ ]    X = reachable
  [ ][ ]    Only (0,0) accessible

Time t=1: Can be at elevation ≤ 1
  [X][ ]    Can move to (1,0)
  [X][ ]

Time t=2: Can be at elevation ≤ 2
  [X][X]    Can move to (0,1)
  [X][ ]

Time t=3: Can be at elevation ≤ 3
  [X][X]    Can finally reach (1,1)
  [X][X]

Answer: 3

---

Union-Find Approach:
Sort all cells by elevation: [(0,0,0), (1,0,1), (0,1,2), (1,1,3)]

Process cells in order:
t=0: Add (0,0), check if (0,0) and (n-1,n-1) connected → No
t=1: Add (1,0), union with (0,0), check connection → No
t=2: Add (0,1), union with (0,0), check connection → No
t=3: Add (1,1), union with (0,1) and (1,0), check connection → Yes!

First time (0,0) and (1,1) are in same component: t=3
```

```
Another example: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

Visual grid:
  0  1  2  3  4
 24 23 22 21  5
 12 13 14 15 16
 11 17 18 19 20
 10  9  8  7  6

Optimal path requires waiting until we can traverse the highest cell in our path.
The path with minimum maximum elevation is 0→1→2→3→4→5→16→20→6
Maximum elevation in this path: 16
```

## Examples

**Example 1:**
```
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
```

**Example 2:**
```
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
```

## Constraints
- n == grid.length
- n == grid[i].length
- 1 <= n <= 50
- 0 <= grid[i][j] < n^2
- Each value grid[i][j] is unique
