# Cheapest Flights Within K Stops (Bellman-Ford Approach)

**Difficulty:** Medium
**LeetCode Link:** [Problem 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

## Description
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

## Visual Representation

```mermaid
graph LR
    A[0] -->|100| B[1]
    A -->|500| C[2]
    B -->|100| C

    src=0, dst=2, k=1

    Path 1: 0 -> 2 (cost: 500, stops: 0)
    Path 2: 0 -> 1 -> 2 (cost: 200, stops: 1) ✓
```

```
Bellman-Ford with K iterations:
- Relax edges at most K+1 times
- Each iteration represents one additional stop
- Can handle negative weights (if any)

Example:
src=0, dst=2, k=1
Iteration 0: [0, ∞, ∞]
Iteration 1: [0, 100, 500]  (direct from src)
Iteration 2: [0, 100, 200]  (via city 1)
Answer: 200
```

## Examples

**Example 1:**
```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation: The optimal path with at most 1 stop is 0 -> 1 -> 3 with cost 100 + 600 = 700.
Note that the path 0 -> 2 -> 3 with cost 100 + 200 = 300 has 2 stops, so it's not allowed.
```

**Example 2:**
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The optimal path with at most 1 stop is 0 -> 1 -> 2 with cost 100 + 100 = 200.
```

**Example 3:**
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The optimal path with 0 stops is 0 -> 2 with cost 500.
```

## Constraints
- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 10^4
- There will not be any multiple flights between two cities
- 0 <= src, dst, k < n
- src != dst

## Algorithm Notes
This problem is ideal for Bellman-Ford because:
- We need to limit the number of edges (stops) in the path
- Standard Dijkstra might find shorter paths with more stops
- Bellman-Ford naturally processes edges in iterations
