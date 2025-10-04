# Find the City With the Smallest Number of Neighbors at a Threshold Distance

**Difficulty:** Medium
**LeetCode Link:** [Problem 1334](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

## Description
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold. If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

## Visual Representation

```mermaid
graph LR
    A[0] ---|2| B[1]
    A ---|4| C[2]
    B ---|3| C
    B ---|1| D[3]
    C ---|5| D

    threshold = 4
```

```
Floyd-Warshall builds all-pairs shortest paths:

Initial distance matrix:
     0   1   2   3
0 [  0   2   4   ∞ ]
1 [  2   0   3   1 ]
2 [  4   3   0   5 ]
3 [  ∞   1   5   0 ]

After Floyd-Warshall:
     0   1   2   3
0 [  0   2   4   3 ]
1 [  2   0   3   1 ]
2 [  4   3   0   4 ]
3 [  3   1   4   0 ]

Cities reachable within threshold=4:
City 0: [1,2,3] → 3 cities
City 1: [0,2,3] → 3 cities
City 2: [0,1,3] → 3 cities
City 3: [0,1,2] → 3 cities

Answer: 3 (highest numbered city with minimum neighbors)
```

## Examples

**Example 1:**
```
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we return city 3 since it has the greatest number.
```

**Example 2:**
```
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1]
City 1 -> [City 0, City 4]
City 2 -> [City 3, City 4]
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
The city 0 has 1 neighboring city at a distanceThreshold = 2.
```

## Constraints
- 2 <= n <= 100
- 1 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 3
- 0 <= fromi < toi < n
- 1 <= weighti, distanceThreshold <= 10^4
- All pairs (fromi, toi) are distinct

## Algorithm Notes
Floyd-Warshall is perfect for this problem because:
- We need all-pairs shortest paths
- n is small (≤ 100), so O(n³) is acceptable
- Simple implementation compared to running Dijkstra n times
