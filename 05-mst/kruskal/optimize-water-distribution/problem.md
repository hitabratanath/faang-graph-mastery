# Optimize Water Distribution in a Village

**Difficulty:** Hard
**LeetCode Link:** [Problem 1168](https://leetcode.com/problems/optimize-water-distribution-in-a-village/)

**Note: This is a LeetCode Premium problem**

## Description
There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional.

Return the minimum total cost to supply water to all houses.

## Visual Representation

```
Example: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]

Houses and Wells:                MST Solution:
   House 1: well cost = 1           [Virtual] Source (0)
   House 2: well cost = 2                |  |  |
   House 3: well cost = 2                1  2  2
                                        /   |   \
Pipes between houses:              House1 House2 House3
   1 <--1--> 2
   2 <--1--> 3

Key Insight: Add a virtual node (source) connected to all houses
             with edge weights equal to well costs.

Graph with Virtual Source:
                Source (0)
                /   |   \
              1/   2|    \2
              /     |     \
         House1   House2  House3
            \       |      /
            1\      |     /1
              \     |    /
               \    |   /
                 \  |  /

MST Construction (Kruskal's):
1. Sort all edges: [(0,1,1), (1,2,1), (2,3,1), (0,2,2), (0,3,2)]
2. Add edge (0,1,1): Connect source to house 1 (build well at house 1)
3. Add edge (1,2,1): Connect house 1 to house 2 (lay pipe)
4. Add edge (2,3,1): Connect house 2 to house 3 (lay pipe)
5. All houses connected!

Total cost: 1 + 1 + 1 = 3
```

## Examples

**Example 1:**
```
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation:
The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1
and connect the other houses to it with cost 2 so the total cost is 3.
```

**Example 2:**
```
Input: n = 2, wells = [1,1], pipes = [[1,2,1]]
Output: 2
Explanation:
We can supply water to both houses by building wells in both houses.
Cost: 1 + 1 = 2
(Building wells is cheaper than: build well in house 1 (1) + pipe (1) = 2)
```

**Example 3:**
```
Input: n = 5, wells = [46012,72474,64965,751,33304], pipes = [[2,1,6719],[3,2,75312],[5,3,44918]]
Output: 131704
Explanation:
Build wells at houses with lower costs and use pipes strategically.
```

## Constraints
- 2 <= n <= 10^4
- wells.length == n
- 0 <= wells[i] <= 10^5
- 1 <= pipes.length <= 10^4
- pipes[j].length == 3
- 1 <= house1j, house2j <= n
- 0 <= costj <= 10^5
- house1j != house2j

## Algorithm Notes
This problem is a classic MST problem with a twist: you can connect to a "virtual source" (building a well) or connect houses to each other (laying pipes). The key insight is to add a virtual node representing the source and treat well costs as edge weights from this source to each house. Then run Kruskal's algorithm on this augmented graph.
