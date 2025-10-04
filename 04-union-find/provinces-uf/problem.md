# Number of Provinces

**Difficulty:** Medium
**LeetCode Link:** [Problem 547](https://leetcode.com/problems/number-of-provinces/)

## Description
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

## Visual Representation

```
Example: isConnected = [[1,1,0],[1,1,0],[0,0,1]]

Cities:      0 --- 1     2

Connected components:
Component 1: {0, 1}
Component 2: {2}

Union-Find Operations:
Initial:    parent = [0, 1, 2]

union(0,1): parent = [0, 0, 2]

Final: 2 distinct roots → 2 provinces
```

```
Adjacency Matrix Visualization:
  0 1 2
0[1 1 0]  City 0 connected to: 0(self), 1
1[1 1 0]  City 1 connected to: 0, 1(self)
2[0 0 1]  City 2 connected to: 2(self)
```

## Examples

**Example 1:**
```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation: Cities 0 and 1 form one province, city 2 forms another province.
```

**Example 2:**
```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: Each city forms its own province (no connections between different cities).
```

## Constraints
- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] is 1 or 0
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]
