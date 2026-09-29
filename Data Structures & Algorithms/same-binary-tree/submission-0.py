# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (q and not p) or (not q and p):
            return False
        if not q and not p:
            return True
        
        if not self.isSameTree(p.right, q.right) or not self.isSameTree(p.left, q.left):
            return False 

        return q.val == p.val
        