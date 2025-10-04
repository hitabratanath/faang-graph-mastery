# Checking Existence of Edge Length Limited Paths

**Difficulty:** Hard
**LeetCode Link:** [Problem 1697](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/)

## Description
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is for each queries[j] to find whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj.

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

## Visual Representation

```
Example: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]

Graph:
    0 ----2---- 1
    |          /|
    8        4  |
    |      /   16
    |    /      |
    2----------/

Edges sorted by distance:
[0,1,2], [1,2,4], [2,0,8], [1,0,16]

Query [0,1,2]:
  Use edges with distance < 2: None
  Can we connect 0 and 1? NO → false

Query [0,2,5]:
  Use edges with distance < 5: [0,1,2], [1,2,4]
  Union-Find:
    union(0,1) → {0,1}
    union(1,2) → {0,1,2}
  Can we connect 0 and 2? YES → true

---

Union-Find with Query Sorting:
1. Sort edges by distance
2. Sort queries by limit (keep original index)
3. For each query in sorted order:
   - Add all edges with distance < limit to Union-Find
   - Check if query endpoints are connected

Processing:
Edges: [0,1,2], [1,2,4], [2,0,8], [1,0,16]
Sorted queries: [0,1,2], [0,2,5]

Query [0,1,2] (limit=2):
  Add edges < 2: (none)
  find(0) ≠ find(1) → false

Query [0,2,5] (limit=5):
  Add edges < 5: [0,1,2], [1,2,4]
  union(0,1), union(1,2)
  find(0) = find(2) → true
```

## Examples

**Example 1:**
```
Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph.
Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true.
```

**Example 2:**
```
Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Explanation:
For query [0,4,14]: Path 0->1->2->3->4 has edges [10,5,9,13], all < 14 → true
For query [1,4,13]: Path 1->2->3->4 has edge 13, not < 13 → false
```

## Constraints
- 2 <= n <= 10^5
- 1 <= edgeList.length, queries.length <= 10^5
- edgeList[i].length == 3
- queries[j].length == 3
- 0 <= ui, vi, pj, qj <= n - 1
- ui != vi
- pj != qj
- 1 <= disi, limitj <= 10^9
- There may be multiple edges between two nodes
