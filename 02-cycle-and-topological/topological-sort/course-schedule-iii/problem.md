# Course Schedule III

**Difficulty:** Hard
**LeetCode Link:** [Problem 630](https://leetcode.com/problems/course-schedule-iii/)

## Description
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

## Visual Representation

```
Example: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]

Timeline visualization:
Day:    0    200   1300  1250     3200
        |-----|-----|-----|--------|
Course 1: [100,200]   ✓ (finish by day 200)
Course 2: [200,1300]  ✓ (finish by day 1300)
Course 4: [2000,3200] ✓ (finish by day 3200)
Course 3: [1000,1250] ✗ (cannot fit)

Greedy approach:
1. Sort by deadline
2. Take courses while time permits
3. If can't fit, replace longest taken course if current is shorter
```

```
Strategy:
Sort courses by deadline: [[100,200],[1000,1250],[200,1300],[2000,3200]]

Take course 1: duration=100, time=100 ✓
Take course 3: duration=1000, time=1100 ✓
Try course 2: duration=200, time=1300, but deadline=1300...
  Current time (1100) + 200 = 1300 ✓
Take course 4: duration=2000, time=3300, deadline=3200 ✗
  Replace longest (1000) with this? No, 2000 > 1000

Result: 3 courses
```

## Examples

**Example 1:**
```
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation:
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
```

**Example 2:**
```
Input: courses = [[1,2]]
Output: 1
```

**Example 3:**
```
Input: courses = [[3,2],[4,3]]
Output: 0
```

## Constraints
- 1 <= courses.length <= 10^4
- 1 <= durationi, lastDayi <= 10^4
