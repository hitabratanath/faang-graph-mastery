# Minimum Knight Moves

**Difficulty:** Medium
**LeetCode Link:** [Problem 1197](https://leetcode.com/problems/minimum-knight-moves/)

## Description
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

## Visual Representation

```
Knight's 8 possible moves:
      2 . 1
      . ♘ .
      3 . 4

  (-2,+1) (+2,+1)
  (-1,+2) (+1,+2)
     ♘
  (-1,-2) (+1,-2)
  (-2,-1) (+2,-1)

Example: [0,0] → [5,5]
[0,0] → [2,1] → [4,2] → [3,4] → [5,5]
Steps: 4
```

## Examples

**Example 1:**
```
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
```

**Example 2:**
```
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
```

## Constraints
- -300 <= x, y <= 300
- 0 <= |x| + |y| <= 300

## Note
This is a LeetCode Premium problem.
