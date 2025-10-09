from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return []

        def dfs(node, path, current_sum):
            if not node: return
            current_sum += node.val
            path.append(node.val)

            if not node.left and not node.right and current_sum == targetSum:
                result.append(path.copy())
            
            dfs(node.left, path, current_sum)
            dfs(node.right, path, current_sum)

            path.pop()
        
        dfs(root, [], 0)
        return result
        