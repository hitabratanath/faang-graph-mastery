# Maximum Students Taking Exam

**Difficulty:** Hard
**LeetCode Link:** [Problem 1349](https://leetcode.com/problems/maximum-students-taking-exam/)

## Description
Given a m x n matrix seats that represents seats in a classroom. The matrix contains:
- '.' represents a good seat
- '#' represents a broken seat

Students may cheat if they sit adjacent to each other (left, right, upper left, upper right, lower left, lower right). You need to find the maximum number of students that can take the exam together without any cheating being possible.

Return the maximum number of students that can take the exam.

## Visual Representation

```
Example: Maximum Students with No Cheating

Classroom Layout:
[["#",".","#","#",".","#"],
 [".","#","#","#","#","."],
 ["#",".","#","#",".","#"]]

Legend:
# = broken seat (cannot sit)
. = available seat
S = student seated

Maximum Flow / Bipartite Matching Approach:

Step 1: Model as Bipartite Graph
- Left set: All valid seats (odd columns)
- Right set: All valid seats (even columns)
- Edge: Connect seats that can "see" each other (would enable cheating)

Step 2: Find Maximum Independent Set
This is equivalent to finding maximum matching in bipartite graph

Visualization of one optimal seating:
[["#","S","#","#",".","#"],
 [".","#","#","#","#","S"],
 ["#","S","#","#",".","#"]]

Students seated: 3 (no two can see each other)

Cheating adjacency (students CANNOT be in these positions simultaneously):
    S1    S2
     \  /
      \/  (diagonal cheat)
      /\
     /  \
    S3    S4


Example 2: Complex Seating
[[".",".",".",".","#"],
 [".",".",".",".","#"],
 [".",".",".",".","."],
 [".",".",".",".","."]]

One optimal arrangement:
[["S",".",".","S","#"],
 [".","S","S",".","#"],
 ["S",".",".","S","."],
 [".","S","S",".",".."]]

Maximum students: 9

Flow network perspective:
- Source connects to all seats
- Each seat has capacity 1
- Edges between "visible" seats
- Find maximum independent set = Total seats - Maximum matching
```

## Examples

**Example 1:**
```
Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam.
```

**Example 2:**
```
Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place students in seats (0,0), (2,2), and (4,0).
```

**Example 3:**
```
Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in seats (0,1), (0,2), (0,3), (1,0), (1,4), (2,0), (2,2), (2,4), (3,0), (3,4).
```

## Constraints
- seats contains only characters '.' and '#'
- m == seats.length
- n == seats[i].length
- 1 <= m <= 8
- 1 <= n <= 8
