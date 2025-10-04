# Satisfiability of Equality Equations

**Difficulty:** Medium
**LeetCode Link:** [Problem 990](https://leetcode.com/problems/satisfiability-of-equality-equations/)

## Description
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi". Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

## Visual Representation

```
Example: equations = ["a==b","b==c","a==c"]

Union-Find Process:

Step 1: Process all equality equations
  "a==b": union(a, b)
    parent: {a→a, b→a, c→c}

  "b==c": union(b, c)
    find(b) = a, find(c) = c
    parent: {a→a, b→a, c→a}

Graph visualization after equalities:
    a
   / \
  b   c   (all in same component)

Step 2: Check all inequality equations
  "a==c": This is an equality, already satisfied

Result: true (all equations satisfied)

---

Counter-example: equations = ["a==b","b!=a"]

Step 1: Process equalities
  "a==b": union(a, b)
    parent: {a→a, b→a}

Step 2: Check inequalities
  "b!=a":
    find(b) = a, find(a) = a
    Same root! But they should be different!

Result: false (contradiction)
```

## Examples

**Example 1:**
```
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
```

**Example 2:**
```
Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
```

**Example 3:**
```
Input: equations = ["a==b","b==c","a==c"]
Output: true
```

**Example 4:**
```
Input: equations = ["a==b","b!=c","c==a"]
Output: false
```

**Example 5:**
```
Input: equations = ["c==c","b==d","x!=z"]
Output: true
```

## Constraints
- 1 <= equations.length <= 500
- equations[i].length == 4
- equations[i][0] is a lowercase letter
- equations[i][1] is either '=' or '!'
- equations[i][2] is '='
- equations[i][3] is a lowercase letter
