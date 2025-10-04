# Most Stones Removed with Same Row or Column

**Difficulty:** Medium
**LeetCode Link:** [Problem 947](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)

## Description
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the maximum number of stones that can be removed.

## Visual Representation

```
Example: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

Grid visualization:
  0 1 2
0 X X .   X = stone
1 X . X   . = empty
2 . X X

Connected components (same row or column):
Component 1: All stones are connected
  (0,0)---(0,1)  (share column 0)
    |       |
  (1,0)---(1,2)  (share row 1)
    |       |
  (2,1)---(2,2)  (share column 1 and 2)

Union-Find perspective:
- Treat each row and column as a node
- Stones connect rows to columns
- Count connected components

Rows: {0, 1, 2}
Cols: {0, 1, 2}

Stone at (0,0): union(row_0, col_0)
Stone at (0,1): union(row_0, col_1)
Stone at (1,0): union(row_1, col_0)
Stone at (1,2): union(row_1, col_2)
Stone at (2,1): union(row_2, col_1)
Stone at (2,2): union(row_2, col_2)

Result: 1 component → can remove (6 - 1) = 5 stones
```

## Examples

**Example 1:**
```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1]
2. Remove stone [2,1] because it shares the same column as [0,1]
3. Remove stone [1,2] because it shares the same row as [1,0]
4. Remove stone [1,0] because it shares the same column as [0,0]
5. Remove stone [0,1] because it shares the same row as [0,0]
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
```

**Example 2:**
```
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves:
1. Remove stone [2,2] because it shares the same row as [2,0]
2. Remove stone [2,0] because it shares the same column as [0,0]
3. Remove stone [0,2] because it shares the same row as [0,0]
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
```

**Example 3:**
```
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
```

## Constraints
- 1 <= stones.length <= 1000
- 0 <= xi, yi <= 10^4
- No two stones are at the same coordinate point
