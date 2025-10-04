# Island Perimeter

**Difficulty:** Easy
**LeetCode Link:** [Problem 463](https://leetcode.com/problems/island-perimeter/)

## Description
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

## Visual Representation

```
Example Grid:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Visual:
. X . .
X X X .
. X . .
X X . .

Perimeter calculation:
. 3 . .      (top cell: 3 sides exposed)
4 X 3 .      (left=4, middle=0, right=3)
. 3 . .      (3 sides exposed)
4 2 . .      (left=4, right=2)

Total perimeter = 3 + 4 + 0 + 3 + 3 + 4 + 2 = 16

Each land cell contributes:
- 4 sides if isolated
- Minus 1 for each adjacent land cell
```

## Examples

**Example 1:**
```
Input: grid = [[0,1,0,0],
               [1,1,1,0],
               [0,1,0,0],
               [1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
```

**Example 2:**
```
Input: grid = [[1]]
Output: 4
```

**Example 3:**
```
Input: grid = [[1,0]]
Output: 4
```

## Constraints
- row == grid.length
- col == grid[i].length
- 1 <= row, col <= 100
- grid[i][j] is 0 or 1
- There is exactly one island in grid
