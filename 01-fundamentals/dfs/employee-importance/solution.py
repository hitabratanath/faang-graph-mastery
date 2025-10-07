from collections import deque
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {emp.id: emp for emp in employees}

        # emp_id
        queue = deque([(id)])
        total_importance = 0
        while queue:
            emp_id = queue.popleft()
            emp = emp_map[emp_id]
            total_importance += emp.importance

            for sub_id in emp.subordinates:
                queue.append(sub_id)

        return total_importance

        