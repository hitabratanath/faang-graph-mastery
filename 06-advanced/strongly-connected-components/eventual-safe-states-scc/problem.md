# Find Eventual Safe States

**Difficulty:** Medium
**LeetCode Link:** [Problem 802](https://leetcode.com/problems/find-eventual-safe-states/)

## Description
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

## Visual Representation

```
Example: Finding Safe States

Graph: [[1,2],[2,3],[5],[0],[5],[],[]]

Directed Graph Visualization:
    0 --> 1 --> 2 --> 5 --> (terminal)
    ↑     |     |
    |     ↓     ↓
    +----- 3    5

    4 --> 5 --> (terminal)

    6 --> (terminal, no outgoing edges)

Analysis:
- Cycle detected: 0 -> 1 -> 3 -> 0 (nodes in cycle are UNSAFE)
- Node 2: Can reach 5 (safe) OR be part of cycle path (UNSAFE)
- Node 4: Leads to 5 (terminal) - SAFE
- Node 5: Terminal node - SAFE
- Node 6: Terminal node - SAFE

Safe States: [2, 4, 5, 6]


Visual State Classification:
    UNSAFE ──> UNSAFE ──> SAFE ──> SAFE
      0         1          2        5
      ↑         |
      |         ↓
      +──── UNSAFE
              3

    SAFE ──> SAFE
      4        5

    SAFE (terminal)
      6
```

## Examples

**Example 1:**
```
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
```

**Example 2:**
```
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation: Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
```

## Constraints
- n == graph.length
- 1 <= n <= 10^4
- 0 <= graph[i].length <= n
- 0 <= graph[i][j] <= n - 1
- graph[i] is sorted in a strictly increasing order
- The graph may contain self-loops
- The number of edges in the graph will be in the range [1, 4 * 10^4]
