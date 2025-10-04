# Critical Connections in a Network

**Difficulty:** Hard
**LeetCode Link:** [Problem 1192](https://leetcode.com/problems/critical-connections-in-a-network/)

## Description
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

## Visual Representation

```
Example: Network with Critical Connections

Graph: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]

Network Diagram:
    0 --- 1 --- 3
     \   /
      \ /
       2

Analysis:
- Triangle (0-1-2): These edges are NOT critical (removing any one still keeps them connected)
- Edge (1-3): This IS critical (removing it disconnects node 3)

Critical Connections (Bridges):
[[1,3]]

Visual with SCC perspective:
    ┌─────┐
    │ SCC │ --- [3]
    │ 0-1-2│
    └─────┘

The triangle forms a strongly connected component.
Edge [1,3] is a bridge connecting the SCC to node 3.


Example 2: Multiple Critical Connections

Graph: n = 6, connections = [[0,1],[1,2],[2,3],[3,4],[4,5]]

Network Diagram:
    0 --- 1 --- 2 --- 3 --- 4 --- 5

All edges are critical connections (it's a chain/tree).
Removing any edge would disconnect the network.

Critical Connections:
[[0,1],[1,2],[2,3],[3,4],[4,5]]
```

## Examples

**Example 1:**
```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
```

**Example 2:**
```
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
```

## Constraints
- 2 <= n <= 10^5
- n - 1 <= connections.length <= 10^5
- 0 <= ai, bi <= n - 1
- ai != bi
- There are no repeated connections
- The graph is connected
