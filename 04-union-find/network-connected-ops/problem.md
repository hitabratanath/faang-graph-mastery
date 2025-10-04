# Number of Operations to Make Network Connected

**Difficulty:** Medium
**LeetCode Link:** [Problem 1319](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

## Description
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

## Visual Representation

```
Example: n = 4, connections = [[0,1],[0,2],[1,2]]

Initial network:
  0---1
  |\ /
  | X
  |/ \
  2

Components: 1 component = {0, 1, 2}, 1 isolated node = {3}
Redundant edges: 1 (the cycle between 0-1-2)

To connect 2 components, we need 1 cable
Available redundant cables: 1
Result: 1 operation (move one redundant cable to connect to node 3)

Final network:
  0---1     3
  |         |
  2---------+

---

Union-Find Analysis:
Initial: parent = [0, 1, 2, 3]

Edge [0,1]: union(0,1) → parent = [0, 0, 2, 3]
Edge [0,2]: union(0,2) → parent = [0, 0, 0, 3]
Edge [1,2]: find(1)=0, find(2)=0 → already connected! (redundant++)

Components: 2 (roots at 0 and 3)
Redundant cables: 1
Cables needed: components - 1 = 2 - 1 = 1

Result: 1 (we have enough redundant cables)
```

## Examples

**Example 1:**
```
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
```

**Example 2:**
```
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Explanation: We have 2 redundant cables and 3 components, so we need 2 cables to connect all.
```

**Example 3:**
```
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables. We have 3 components but only 1 redundant cable.
```

## Constraints
- 1 <= n <= 10^5
- 1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
- connections[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated connections
- No two computers are connected by more than one cable
