# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # use dfs and check if you are a leaf node, if you are and your value = target return None
        # otherwise continue
        def dfs(node: TreeNode):
            if not node:
                return None
                
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            
            if not node.right and not node.left and node.val == target:
                return None
            
            return node
        return dfs(root)