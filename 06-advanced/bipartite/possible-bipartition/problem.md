# Possible Bipartition

**Difficulty:** Medium
**LeetCode Link:** [Problem 886](https://leetcode.com/problems/possible-bipartition/)

## Description
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

## Visual Representation

```
Example 1: Can Bipartition
n = 4, dislikes = [[1,2],[1,3],[2,4]]

Dislike Graph:
    1 --- 2
    |      \
    |       \
    3        4

Bipartition Assignment:
Group A (Red):   1, 4
Group B (Blue):  2, 3

    [A] --- [B]
     |        \
     |         \
    [B]       [A]

Result: true (successful bipartition)


Example 2: Cannot Bipartition
n = 3, dislikes = [[1,2],[1,3],[2,3]]

Dislike Graph (Triangle):
    1 --- 2
     \   /
      \ /
       3

This forms an odd cycle (triangle), which cannot be bipartitioned.

Result: false (impossible to bipartition)
```

## Examples

**Example 1:**
```
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group can be [1,4] and the second group can be [2,3].
```

**Example 2:**
```
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.
```

**Example 3:**
```
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
Explanation: The dislike relationships form a cycle of odd length (5), making bipartition impossible.
```

## Constraints
- 1 <= n <= 2000
- 0 <= dislikes.length <= 10^4
- dislikes[i].length == 2
- 1 <= ai < bi <= n
- All the pairs of dislikes are unique
