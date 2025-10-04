# Number of Good Paths

**Difficulty:** Hard
**LeetCode Link:** [Problem 2421](https://leetcode.com/problems/number-of-good-paths/)

## Description
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:
1. The starting node and the ending node have the same value.
2. All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).

Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.

## Visual Representation

```
Example: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]

Tree structure:
        0(1)
       / \
    1(3)  2(2)
         / \
      3(1) 4(3)

Good paths analysis:

Value 1 nodes: {0, 3}
- Path [0]: value 1 → count 1
- Path [3]: value 1 → count 1
- Path [0→2→3]: max=2 > 1 → NOT good

Value 2 nodes: {2}
- Path [2]: value 2 → count 1

Value 3 nodes: {1, 4}
- Path [1]: value 3 → count 1
- Path [4]: value 3 → count 1
- Path [1→0→2→4]: max along path 0(1), 2(2) both ≤ 3 → GOOD! count 1

Total: 6 good paths

---

Union-Find Approach:
Process nodes by value in ascending order:

Value 1: nodes {0, 3}
  Add node 0, add node 3
  Components: {0}, {3}
  Good paths with max value 1: 1 + 1 = 2

Value 2: node {2}
  Add node 2, connect to 0 (edge [0,2], both nodes added)
  Components: {0, 2}, {3}
  Good paths with max value 2: 1

Value 3: nodes {1, 4}
  Add node 1, connect to 0 (edge [0,1])
  Add node 4, connect to 2 (edge [2,4])
  Now 1 and 4 are in same component through {1-0-2-4}
  Good paths with max value 3: 1 + 1 + 1 = 3
    (self-1, self-4, 1-to-4)

Total: 2 + 1 + 3 = 6
```

## Examples

**Example 1:**
```
Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 6 good paths:
- 0
- 1
- 2
- 3
- 4
- 1 -> 0 -> 2 -> 4
```

**Example 2:**
```
Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 7 good paths:
- 0
- 1
- 2
- 3
- 4
- 0 -> 1 (both value 1)
- 2 -> 3 (both value 2)
```

**Example 3:**
```
Input: vals = [1], edges = []
Output: 1
Explanation: The only good path is the single node itself.
```

## Constraints
- n == vals.length
- 1 <= n <= 3 * 10^4
- 0 <= vals[i] <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- edges represents a valid tree
