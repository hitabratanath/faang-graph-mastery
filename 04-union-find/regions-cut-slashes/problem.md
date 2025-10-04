# Regions Cut By Slashes

**Difficulty:** Medium
**LeetCode Link:** [Problem 959](https://leetcode.com/problems/regions-cut-by-slashes/)

## Description
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

## Visual Representation

```
Example: grid = [" /","/ "]

Original 2x2 grid:
+--+--+
|  /|  |
+--+--+
| /  |  |
+--+--+

Divide each cell into 4 triangles (N, E, S, W):
Each 1x1 cell becomes:
    N
   /|\
  W-+-E
   \|/
    S

Grid transformation:
Cell (0,0) = " /":     Cell (0,1) = "  ":     Cell (1,0) = "/ ":     Cell (1,1) = "  ":
    N                      N                      N                      N
   / \                    | |                    /|\                    | |
  W---E                  W---E                  W-+-E                  W---E
   \ /                    | |                    \|/                    | |
    S                      S                      S                      S
  N-E-S-W united         All united             N|E, S|W united        All united

Union-Find Operations:
- ' ' (space): unite all 4 triangles
- '/' (slash): unite N-W, unite E-S
- '\' (backslash): unite N-E, unite S-W
- Connect adjacent cells across boundaries

Result: 5 regions
```

```
Visual breakdown of " /":
+---+
| /↗|   North-West are together
|/  |   East-South are together
+---+   = 2 regions in this cell

Visual breakdown of "/ ":
+---+
|↖\ |   North-East are together
|  \|   South-West are together
+---+   = 2 regions in this cell
```

## Examples

**Example 1:**
```
Input: grid = [" /","/ "]
Output: 2
```

**Example 2:**
```
Input: grid = [" /","  "]
Output: 1
```

**Example 3:**
```
Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
```

## Constraints
- n == grid.length == grid[i].length
- 1 <= n <= 30
- grid[i][j] is either '/', '\', or ' '
