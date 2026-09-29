# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            include_left, skip_left = dfs(node.left)
            include_right, skip_right = dfs(node.right)
            include = skip_left + skip_right + node.val
            skip = max(include_left, skip_left) + max(include_right, skip_right)
            return (include, skip)
        return max(dfs(root))
            