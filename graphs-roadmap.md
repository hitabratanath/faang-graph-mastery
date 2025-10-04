# Graph Algorithms Roadmap for FAANG Interviews

## Study Order & Timeline
Follow this sequence for optimal learning progression. Spend 1-2 weeks on each section.

---

## Week 1-2: Fundamentals & Traversal

### 1. Graph Representation & Basics
**Concepts:** Adjacency list, adjacency matrix, edge list, directed/undirected graphs

**Easy Questions:**
- [ ] Number of Islands (LeetCode 200)
- [ ] Find Center of Star Graph (LeetCode 1791)
- [ ] Find if Path Exists in Graph (LeetCode 1971)
- [ ] Find the Town Judge (LeetCode 997)

**Medium Questions:**
- [ ] Clone Graph (LeetCode 133)
- [ ] Number of Provinces (LeetCode 547)
- [ ] Keys and Rooms (LeetCode 841)

---

### 2. BFS (Breadth-First Search)
**Concepts:** Queue-based traversal, level-order processing, shortest path in unweighted graphs

**Easy Questions:**
- [ ] Binary Tree Level Order Traversal (LeetCode 102)
- [ ] Average of Levels in Binary Tree (LeetCode 637)
- [ ] Flood Fill (LeetCode 733)
- [ ] N-ary Tree Level Order Traversal (LeetCode 429)

**Medium Questions:**
- [ ] Rotting Oranges (LeetCode 994)
- [ ] 01 Matrix (LeetCode 542)
- [ ] As Far from Land as Possible (LeetCode 1162)
- [ ] Shortest Path in Binary Matrix (LeetCode 1091)
- [ ] Word Ladder (LeetCode 127)
- [ ] Open the Lock (LeetCode 752)
- [ ] Minimum Knight Moves (LeetCode 1197)
- [ ] Shortest Bridge (LeetCode 934)

**Hard Questions:**
- [ ] Word Ladder II (LeetCode 126)
- [ ] Minimum Cost to Make at Least One Valid Path (LeetCode 1368)

---

### 3. DFS (Depth-First Search)
**Concepts:** Stack/recursion-based traversal, backtracking, cycle detection

**Easy Questions:**
- [ ] Max Area of Island (LeetCode 695)
- [ ] Island Perimeter (LeetCode 463)
- [ ] Employee Importance (LeetCode 690)

**Medium Questions:**
- [ ] Number of Islands (LeetCode 200) - revisit with DFS
- [ ] Pacific Atlantic Water Flow (LeetCode 417)
- [ ] Surrounded Regions (LeetCode 130)
- [ ] Number of Enclaves (LeetCode 1020)
- [ ] Number of Closed Islands (LeetCode 1254)
- [ ] Time Needed to Inform All Employees (LeetCode 1376)
- [ ] Count Sub Islands (LeetCode 1905)
- [ ] All Paths From Source to Target (LeetCode 797)
- [ ] Path Sum II (LeetCode 113)

**Hard Questions:**
- [ ] Making a Large Island (LeetCode 827)
- [ ] Number of Distinct Islands (LeetCode 711) - Premium

---

## Week 3: Cycle Detection & Topological Sort

### 4. Cycle Detection
**Concepts:** Detect cycles using DFS colors (white/gray/black), Union-Find

**Medium Questions:**
- [ ] Course Schedule (LeetCode 207)
- [ ] Detect Cycle in Directed Graph (GeeksforGeeks)
- [ ] Find Eventual Safe States (LeetCode 802)
- [ ] Redundant Connection (LeetCode 684)
- [ ] Redundant Connection II (LeetCode 685)

---

### 5. Topological Sort
**Concepts:** Kahn's algorithm (BFS), DFS-based topological sort, dependency resolution

**Medium Questions:**
- [ ] Course Schedule II (LeetCode 210)
- [ ] Minimum Height Trees (LeetCode 310)
- [ ] Sort Items by Groups Respecting Dependencies (LeetCode 1203)
- [ ] Alien Dictionary (LeetCode 269) - Premium
- [ ] Sequence Reconstruction (LeetCode 444) - Premium
- [ ] Parallel Courses (LeetCode 1136) - Premium

**Hard Questions:**
- [ ] Course Schedule III (LeetCode 630)
- [ ] Parallel Courses II (LeetCode 1494)

---

## Week 4: Shortest Path Algorithms

### 6. Dijkstra's Algorithm
**Concepts:** Single-source shortest path, priority queue, non-negative weights

**Medium Questions:**
- [ ] Network Delay Time (LeetCode 743)
- [ ] Path with Maximum Probability (LeetCode 1514)
- [ ] Path with Minimum Effort (LeetCode 1631)
- [ ] Cheapest Flights Within K Stops (LeetCode 787)
- [ ] Swim in Rising Water (LeetCode 778)
- [ ] Minimum Cost to Reach Destination in Time (LeetCode 1928)

**Hard Questions:**
- [ ] Reachable Nodes In Subdivided Graph (LeetCode 882)
- [ ] Minimum Weighted Subgraph With the Required Paths (LeetCode 2203)

---

### 7. Bellman-Ford Algorithm
**Concepts:** Handles negative weights, detects negative cycles

**Medium Questions:**
- [ ] Cheapest Flights Within K Stops (LeetCode 787) - alternative approach
- [ ] Network Delay Time (LeetCode 743) - alternative approach

---

### 8. Floyd-Warshall Algorithm
**Concepts:** All-pairs shortest path, DP approach

**Medium Questions:**
- [ ] Find the City With the Smallest Number of Neighbors at a Threshold Distance (LeetCode 1334)
- [ ] Minimum Cost to Make at Least One Valid Path (LeetCode 1368)

**Hard Questions:**
- [ ] Find All People With Secret (LeetCode 2092)

---

## Week 5: Union-Find (Disjoint Set Union)

### 9. Union-Find / DSU
**Concepts:** Path compression, union by rank/size, connected components

**Medium Questions:**
- [ ] Number of Provinces (LeetCode 547) - revisit with Union-Find
- [ ] Redundant Connection (LeetCode 684)
- [ ] Most Stones Removed with Same Row or Column (LeetCode 947)
- [ ] Accounts Merge (LeetCode 721)
- [ ] Satisfiability of Equality Equations (LeetCode 990)
- [ ] Regions Cut By Slashes (LeetCode 959)
- [ ] Number of Operations to Make Network Connected (LeetCode 1319)
- [ ] Smallest String With Swaps (LeetCode 1202)

**Hard Questions:**
- [ ] Swim in Rising Water (LeetCode 778) - alternative approach
- [ ] Checking Existence of Edge Length Limited Paths (LeetCode 1697)
- [ ] Number of Good Paths (LeetCode 2421)

---

## Week 6: Minimum Spanning Tree

### 10. MST - Kruskal's & Prim's
**Concepts:** Minimum spanning tree, Kruskal's with Union-Find, Prim's with priority queue

**Medium Questions:**
- [ ] Min Cost to Connect All Points (LeetCode 1584)
- [ ] Optimize Water Distribution in a Village (LeetCode 1168) - Premium

**Hard Questions:**
- [ ] Find Critical and Pseudo-Critical Edges in MST (LeetCode 1489)

---

## Week 7-8: Advanced Topics

### 11. Bipartite Graphs
**Concepts:** Two-coloring, BFS/DFS coloring

**Medium Questions:**
- [ ] Is Graph Bipartite? (LeetCode 785)
- [ ] Possible Bipartition (LeetCode 886)

---

### 12. Strongly Connected Components
**Concepts:** Kosaraju's algorithm, Tarjan's algorithm

**Medium Questions:**
- [ ] Critical Connections in a Network (LeetCode 1192)
- [ ] Find Eventual Safe States (LeetCode 802) - revisit

---

### 13. Articulation Points & Bridges
**Concepts:** Cut vertices, cut edges, Tarjan's algorithm

**Hard Questions:**
- [ ] Critical Connections in a Network (LeetCode 1192)

---

### 14. Graph Coloring
**Concepts:** Chromatic number, greedy coloring

**Hard Questions:**
- [ ] Flower Planting With No Adjacent (LeetCode 1042)

---

### 15. Maximum Flow / Minimum Cut
**Concepts:** Ford-Fulkerson, Edmonds-Karp, max-flow min-cut theorem

**Hard Questions:**
- [ ] Maximum Students Taking Exam (LeetCode 1349)
- [ ] Minimum Number of Days to Disconnect Island (LeetCode 1568)

---

## Common Patterns & Problem Types

### Island/Grid Problems
- [ ] Max Area of Island (LeetCode 695)
- [ ] Number of Islands (LeetCode 200)
- [ ] Number of Closed Islands (LeetCode 1254)
- [ ] Number of Distinct Islands (LeetCode 711)
- [ ] Making a Large Island (LeetCode 827)

### Matrix/Grid Traversal
- [ ] Shortest Path in Binary Matrix (LeetCode 1091)
- [ ] Shortest Path to Get All Keys (LeetCode 864)
- [ ] Shortest Distance from All Buildings (LeetCode 317) - Premium

### Transformation/Word Ladder
- [ ] Word Ladder (LeetCode 127)
- [ ] Word Ladder II (LeetCode 126)
- [ ] Minimum Genetic Mutation (LeetCode 433)

### Dependency/Schedule Problems
- [ ] Course Schedule (LeetCode 207)
- [ ] Course Schedule II (LeetCode 210)
- [ ] Task Scheduler (LeetCode 621)

### Clone/Copy Problems
- [ ] Clone Graph (LeetCode 133)
- [ ] Copy List with Random Pointer (LeetCode 138)

---

## Additional Practice (Bonus)

### Hard Mixed Questions
- [ ] Reconstruct Itinerary (LeetCode 332)
- [ ] Bus Routes (LeetCode 815)
- [ ] Sliding Puzzle (LeetCode 773)
- [ ] Shortest Path Visiting All Nodes (LeetCode 847)
- [ ] Minimize Malware Spread (LeetCode 924)
- [ ] Minimize Malware Spread II (LeetCode 928)
- [ ] Longest Increasing Path in a Matrix (LeetCode 329)
- [ ] Frog Position After T Seconds (LeetCode 1377)
- [ ] Minimum Number of Flips to Convert Binary Matrix (LeetCode 1284)

---

## Key Tips for FAANG Interviews

1. **Master BFS & DFS first** - They're the foundation for 70% of graph problems
2. **Practice graph construction** - Many problems require building the graph from input
3. **Know time/space complexity** - Be able to explain O(V+E) for traversal
4. **Multiple approaches** - Some problems can be solved with BFS, DFS, or Union-Find
5. **Edge cases:** Empty graphs, disconnected components, self-loops, duplicate edges
6. **Communication:** Explain your approach before coding, discuss tradeoffs

## Complexity Cheat Sheet

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| BFS/DFS | O(V + E) | O(V) |
| Dijkstra's | O((V + E) log V) | O(V) |
| Bellman-Ford | O(V × E) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Kruskal's MST | O(E log E) | O(V) |
| Prim's MST | O((V + E) log V) | O(V) |
| Topological Sort | O(V + E) | O(V) |
| Union-Find | O(α(n)) ≈ O(1) | O(V) |

---

## Progress Tracking
- Total Easy: ~15 problems
- Total Medium: ~70 problems
- Total Hard: ~25 problems
- **Total: ~110 problems**

Good luck with your FAANG interview preparation! 🚀
