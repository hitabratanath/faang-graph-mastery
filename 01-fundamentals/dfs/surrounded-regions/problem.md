# Surrounded Regions

**Difficulty:** Medium
**LeetCode Link:** [Problem 130](https://leetcode.com/problems/surrounded-regions/)

## Description
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

## Visual Representation

```
Input board:
X X X X
X O O X
X X O X
X O X X

After capturing:
X X X X
X X X X
X X X X
X O X X

Explanation:
- The top-left O's are surrounded by X's, so they are captured
- The bottom O is on the border, so it's NOT captured
- Any O connected to a border O is also NOT captured

Step-by-step visualization:
1. Original:              2. Border O's (safe):    3. After capture:
   X X X X                   X X X X                  X X X X
   X O O X                   X . . X                  X X X X
   X X O X                   X X . X                  X X X X
   X O X X                   X O X X                  X O X X

   (O's connected to border remain as O, others become X)
```

## Examples

**Example 1:**
```
Input: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]
Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
```

**Example 2:**
```
Input: board = [["X"]]
Output: [["X"]]
```

## Constraints
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'
