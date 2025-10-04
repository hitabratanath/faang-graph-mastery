# Min Cost to Connect All Points

**Difficulty:** Medium
**LeetCode Link:** [Problem 1584](https://leetcode.com/problems/min-cost-to-connect-all-points/)

## Description
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

## Visual Representation

```
Example: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

All Points:             MST (Minimum Spanning Tree):
    (3,10)                     (3,10)
      *                          *
                                 |
                                 | 8
                                 |
(0,0) * --- * (2,2)          (0,0) * --- * (2,2)
        \   / \                      \       \
         \ /   \                      \ 2     \ 3
          X     * (5,2)                \       \
         / \   /                        * (7,0) * (5,2)
        /   \ /
       /     * (7,0)

Edge weights (Manhattan distances):
(0,0) -> (2,2): |0-2| + |0-2| = 4
(2,2) -> (3,10): |2-3| + |2-10| = 9
(2,2) -> (5,2): |2-5| + |2-2| = 3
(5,2) -> (7,0): |5-7| + |2-0| = 4
(0,0) -> (7,0): |0-7| + |0-0| = 7

MST includes edges: (2,2)->(5,2)=3, (0,0)->(2,2)=4, (5,2)->(7,0)=4, (2,2)->(3,10)=9
Total cost: 3 + 4 + 4 + 9 = 20

Kruskal's Algorithm Steps:
1. Calculate all edge weights (Manhattan distances)
2. Sort edges by weight
3. Use Union-Find to avoid cycles
4. Add edges until all points connected
```

## Examples

**Example 1:**
```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:**
```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
Explanation:
Connect points:
(-4,1) -> (-2,5): |-4-(-2)| + |1-5| = 2 + 4 = 6
(-2,5) -> (3,12): |-2-3| + |5-12| = 5 + 7 = 12
Total: 6 + 12 = 18
```

**Example 3:**
```
Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
Explanation:
Minimum spanning tree connects all 4 points with total cost 4.
```

## Constraints
- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs (xi, yi) are distinct
