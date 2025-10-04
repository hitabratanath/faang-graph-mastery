# Redundant Connection

**Difficulty:** Medium
**LeetCode Link:** [Problem 684](https://leetcode.com/problems/redundant-connection/)

## Description
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

## Visual Representation

```
Example: edges = [[1,2],[1,3],[2,3]]

Step-by-step Union-Find:
Initial state: parent = [0, 1, 2, 3]

Edge [1,2]:
  find(1) = 1, find(2) = 2  (different roots)
  union(1,2) → parent = [0, 1, 1, 3]
  Graph: 1---2   3

Edge [1,3]:
  find(1) = 1, find(3) = 3  (different roots)
  union(1,3) → parent = [0, 1, 1, 1]
  Graph: 1---2
         |
         3

Edge [2,3]:
  find(2) = 1, find(3) = 1  (same root!)
  CYCLE DETECTED! Return [2,3]

  Adding [2,3] would create:
  1---2
  |\ /|
  | X |  ← cycle formed
  |/ \|
  3---+
```

## Examples

**Example 1:**
```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Explanation: The edge [2,3] creates a cycle in the graph.
```

**Example 2:**
```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
Explanation: The edge [1,4] is the last edge that creates a cycle.
```

## Constraints
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges
- The given graph is connected
