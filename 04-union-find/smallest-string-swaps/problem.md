# Smallest String With Swaps

**Difficulty:** Medium
**LeetCode Link:** [Problem 1202](https://leetcode.com/problems/smallest-string-with-swaps/)

## Description
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

## Visual Representation

```
Example: s = "dcab", pairs = [[0,3],[1,2]]

Initial string:
Index:  0  1  2  3
Char:   d  c  a  b

Pairs create connections:
[0,3]: index 0 ↔ index 3
[1,2]: index 1 ↔ index 2

Union-Find groups:
Group 1: {0, 3} → chars {d, b}
Group 2: {1, 2} → chars {c, a}

Within each group, we can arrange characters in any order!
Group 1: {d, b} → sort to {b, d}
Group 2: {c, a} → sort to {a, c}

Place sorted characters back:
Index:  0  1  2  3
Group:  1  2  2  1
Sorted: b  a  c  d

Result: "bacd"

---

Union-Find Process:
Initial: parent = [0, 1, 2, 3]

Pair [0,3]: union(0, 3)
  parent = [0, 1, 2, 0]  (0 and 3 connected)

Pair [1,2]: union(1, 2)
  parent = [0, 1, 1, 0]  (1 and 2 connected)

Components:
  Component 0: {0, 3}
  Component 1: {1, 2}
```

## Examples

**Example 1:**
```
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explanation:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
```

**Example 2:**
```
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explanation:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Note: [0,3] and [0,2] create transitive connection [2,3], so all indices {0,1,2,3} are in one group.
All characters can be rearranged: {d,c,a,b} → {a,b,c,d}
```

**Example 3:**
```
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explanation:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

All indices are transitively connected, so we can achieve any permutation.
```

## Constraints
- 1 <= s.length <= 10^5
- 0 <= pairs.length <= 10^5
- 0 <= pairs[i][0], pairs[i][1] < s.length
- s only contains lowercase English letters
