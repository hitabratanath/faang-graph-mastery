from collections import deque
from typing import Lists

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = deque([root])

        while queue:
            sum = 0
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:    
                    queue.append(node.right)
            result.append(sum / n)

        return result