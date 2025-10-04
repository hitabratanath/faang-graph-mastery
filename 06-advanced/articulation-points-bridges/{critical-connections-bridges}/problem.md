# Critical Connections in a Network

**Difficulty:** Hard
**LeetCode Link:** [Problem 1192](https://leetcode.com/problems/critical-connections-in-a-network/)

## Description
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

## Visual Representation

```
Example: Finding Bridges (Critical Connections)

Graph: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]

Network Diagram:
    0 --- 1 --- 3
     \   /
      \ /
       2

Bridge Detection using Tarjan's Algorithm:
- Discovery time: Time when node is first visited
- Low-link value: Lowest discovery time reachable from node

Step-by-step:
1. Start DFS from node 0
   disc[0] = 0, low[0] = 0

2. Visit node 1
   disc[1] = 1, low[1] = 1

3. Visit node 2
   disc[2] = 2, low[2] = 2

4. Back edge to node 0
   low[2] = min(low[2], disc[0]) = 0
   low[1] = min(low[1], low[2]) = 0

5. Visit node 3 from node 1
   disc[3] = 3, low[3] = 3

6. Check: low[3] > disc[1]?
   Yes! Edge (1,3) is a bridge

Visual with Discovery/Low values:
    0 (0,0) --- 1 (1,0) --- 3 (3,3)
     \         /               ↑
      \       /          BRIDGE (low[3] > disc[1])
       2 (2,0)

Critical Connections (Bridges): [[1,3]]


Example 2: Tree Structure (All Edges are Bridges)

Graph: n = 5, connections = [[0,1],[1,2],[1,3],[3,4]]

         0
         |
         1
        / \
       2   3
           |
           4

Every edge is a bridge because there's only one path between any two nodes.
Critical Connections: [[0,1],[1,2],[1,3],[3,4]]
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
