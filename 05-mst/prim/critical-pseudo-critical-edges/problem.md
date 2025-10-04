# Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

**Difficulty:** Hard
**LeetCode Link:** [Problem 1489](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

## Description
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

## Visual Representation

```
Example: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]

Graph with edge indices:
        0 ---1--- 1
        |    e0   |
       2|         |1
       e3        e1
        |         |
        3 ---2--- 2
        |\   e2  /
      3| | \    |6
      e5|  \   |e6
        |  3\  |
        4    \ |
         \e4  \|
          ----  1

Edge list with indices:
e0: [0,1,1]  weight=1
e1: [1,2,1]  weight=1
e2: [2,3,2]  weight=2
e3: [0,3,2]  weight=2
e4: [0,4,3]  weight=3
e5: [3,4,3]  weight=3
e6: [1,4,6]  weight=6

MST weight: 1 + 1 + 2 + 3 = 7

Possible MSTs:
MST 1: edges {0,1,2,4} - uses e0,e1,e2,e4
MST 2: edges {0,1,2,5} - uses e0,e1,e2,e5
MST 3: edges {0,1,3,4} - uses e0,e1,e3,e4
MST 4: edges {0,1,3,5} - uses e0,e1,e3,e5

Critical edges (appear in ALL MSTs):
- Edge 0 [0,1,1]: Removing increases MST weight to 8
- Edge 1 [1,2,1]: Removing increases MST weight to 8

Pseudo-critical edges (appear in SOME but not ALL MSTs):
- Edge 2 [2,3,2]: Can be in MST or replaced by edge 3
- Edge 3 [0,3,2]: Can be in MST or replaced by edge 2
- Edge 4 [0,4,3]: Can be in MST or replaced by edge 5
- Edge 5 [3,4,3]: Can be in MST or replaced by edge 4

Non-critical edges:
- Edge 6 [1,4,6]: Never in any MST (too expensive)

Testing Process:
1. Find original MST weight
2. For each edge:
   - Test critical: Remove edge, compute MST
     If MST weight increases or graph disconnected -> Critical
   - Test pseudo-critical: Force include edge, compute MST
     If MST weight unchanged -> Pseudo-critical
```

## Examples

**Example 1:**
```
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation:
Critical edges: [0,1]
Pseudo-critical edges: [2,3,4,5]
```

**Example 2:**
```
Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation:
All edges form a cycle with equal weights, so any 3 edges form an MST.
No critical edges exist.
All edges are pseudo-critical.
```

**Example 3:**
```
Input: n = 3, edges = [[0,1,1],[1,2,2],[0,2,3]]
Output: [[0,1],[]]
Explanation:
Edge 0 [0,1,1] is critical
Edge 1 [1,2,2] is critical
Edge 2 [0,2,3] is not in MST (weight too high)
No pseudo-critical edges
```

## Constraints
- 2 <= n <= 100
- 1 <= edges.length <= min(200, n * (n - 1) / 2)
- edges[i].length == 3
- 0 <= ai < bi < n
- 1 <= weighti <= 1000
- All pairs (ai, bi) are distinct

## Algorithm Notes
Use Kruskal's algorithm with Union-Find three times for each edge:
1. First, find the original MST weight
2. For critical edge test: Skip the edge and build MST without it
   - If MST weight increases or graph disconnected, edge is critical
3. For pseudo-critical edge test: Force include the edge first, then build rest of MST
   - If final MST weight equals original, edge is pseudo-critical
