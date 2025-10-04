# Shortest Path to Get All Keys

**Difficulty:** Hard
**LeetCode Link:** [Problem 864](https://leetcode.com/problems/shortest-path-to-get-all-keys/)

## Description
You are given an m x n grid grid where:
- '.' is an empty cell
- '#' is a wall
- '@' is the starting point
- Lowercase letters represent keys
- Uppercase letters represent locks

You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

## Visual Representation

```
Grid:
@ . a
. # .
b . A

State space exploration:
Position: (0,0), Keys: {}
   ↓
Position: (0,1), Keys: {}
   ↓
Position: (0,2), Keys: {a}  ← Picked up key 'a'
   ↓
Position: (1,2), Keys: {a}
   ↓
Position: (2,2), Keys: {a}  ← Can now pass through lock 'A'
   ↓
Position: (2,1), Keys: {a}
   ↓
Position: (2,0), Keys: {a,b} ← Picked up key 'b'

Total moves: 8
```

## Examples

**Example 1:**
```
Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys, not to open all the locks.
```

**Example 2:**
```
Input: grid = ["@..aA","..B#.","....b"]
Output: 6
```

**Example 3:**
```
Input: grid = ["@Aa"]
Output: -1
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 30
- grid[i][j] is either an English letter, '.', '#', or '@'
- There is exactly one '@' in the grid
- The number of keys in the grid is in the range [1, 6]
- Each key in the grid is unique
- Each key in the grid has a matching lock
