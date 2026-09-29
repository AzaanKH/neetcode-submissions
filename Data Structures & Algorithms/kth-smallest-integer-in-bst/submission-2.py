# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node is None:
                return None
            
            # Traverse the left subtree
            left = inorder(node.left)
            if left is not None:
                return left
            
            # Visit the current node
            nonlocal count
            count += 1
            if count == k:
                return node.val
            
            # Traverse the right subtree
            return inorder(node.right)

        count = 0
        return inorder(root)



        