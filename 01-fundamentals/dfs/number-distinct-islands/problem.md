# Number of Distinct Islands

**Difficulty:** Medium (Premium)
**LeetCode Link:** [Problem 711](https://leetcode.com/problems/number-of-distinct-islands/)

## Description
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (not rotated or reflected) to equal the other.

Return the number of distinct islands.

## Visual Representation

```
Input grid:
[[1,1,0,0,0],
 [1,1,0,0,0],
 [0,0,0,1,1],
 [0,0,0,1,1]]

Islands visualization:
X X . . .     Island 1: shape = [(0,0), (0,1), (1,0), (1,1)]
X X . . .                        or "DRRU" pattern
. . . X X     Island 2: shape = [(0,0), (0,1), (1,0), (1,1)]
. . . X X                        or "DRRU" pattern

Both islands have the SAME shape (just translated)
Answer: 1 distinct island

Another example:
[[1,1,0,1,1],
 [1,0,0,0,0],
 [0,0,0,0,1],
 [1,1,0,1,1]]

X X . X X     Island 1: [(0,0), (0,1), (1,0)] = "DL"
X . . . .     Island 2: [(0,0), (0,1)] = "R"
. . . . X     Island 3: [(0,0)] = single cell
X X . X X     Island 4: [(0,0), (0,1), (1,0)] = "DL"
              Island 5: [(0,0), (0,1)] = "R"

Distinct shapes:
- Shape "DL": appears twice (islands 1 and 4)
- Shape "R": appears twice (islands 2 and 5)
- Single cell: appears once (island 3)
Answer: 3 distinct islands

Shape encoding example:
Starting from any cell in island, record moves:
D = Down, U = Up, R = Right, L = Left, X = Start

Island pattern:
X X
X

Can be encoded as:
- Start at (0,0): X
- Right to (0,1): R
- Down to (1,0): D
- Pattern: "XRD" or use coordinate offsets: [(0,0), (0,1), (1,0)]
```

## Examples

**Example 1:**
```
Input: grid = [[1,1,0,0,0],
               [1,1,0,0,0],
               [0,0,0,1,1],
               [0,0,0,1,1]]
Output: 1
```

**Example 2:**
```
Input: grid = [[1,1,0,1,1],
               [1,0,0,0,0],
               [0,0,0,0,1],
               [1,1,0,1,1]]
Output: 3
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1
