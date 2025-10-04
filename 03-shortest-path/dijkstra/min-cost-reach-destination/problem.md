# Minimum Cost to Reach Destination in Time

**Difficulty:** Hard
**LeetCode Link:** [Problem 1928](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/)

## Description
There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

Each time you pass through a city, you must pay a passing fee of that city, represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you need to pay when you pass through city j.

In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the sum of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).

Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.

## Visual Representation

```
City Network:
    0 ---10min---> 1
    |              |
  10min          10min
    |              |
    v              v
    2 ---10min---> 3

Passing Fees: [5, 1, 2, 20]
MaxTime: 30

Paths from 0 to 3:
1) 0 -> 1 -> 3
   Time: 10 + 10 = 20 minutes ✓
   Cost: 5 + 1 + 20 = 26 dollars

2) 0 -> 2 -> 3
   Time: 10 + 10 = 20 minutes ✓
   Cost: 5 + 2 + 20 = 27 dollars

3) 0 -> 1 -> 2 -> 3
   Time: 10 + ? + 10 (may exceed maxTime)

Minimum cost: 26 dollars (path 1)
```

```
Example with time constraint:
Cities: 0 ---5min---> 1 ---25min---> 2
Fees:  [1,          2,            3]
MaxTime: 29

Direct path 0->1->2:
Time: 5 + 25 = 30 minutes (exceeds maxTime=29) ✗

No valid path exists → return -1
```

## Examples

**Example 1:**
```
Input: maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: 11
Explanation: The path to take is 0 -> 1 -> 2 -> 5. (0 indexed)
Time taken: 10 + 10 + 10 = 30
Cost: 5 + 1 + 2 + 3 = 11
```

**Example 2:**
```
Input: maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: 48
Explanation: The path to take is 0 -> 3 -> 4 -> 5. (0 indexed)
Time taken: 1 + 10 + 15 = 26
Cost: 5 + 20 + 20 + 3 = 48
```

**Example 3:**
```
Input: maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: -1
Explanation: It is impossible to complete the journey within 25 minutes.
```

## Constraints
- 1 <= maxTime <= 1000
- n == passingFees.length
- 2 <= n <= 1000
- n - 1 <= edges.length <= 1000
- 0 <= xi, yi <= n - 1
- 1 <= timei <= 1000
- 1 <= passingFees[j] <= 1000
- The graph may contain multiple edges between two nodes
- The graph does not contain self loops
