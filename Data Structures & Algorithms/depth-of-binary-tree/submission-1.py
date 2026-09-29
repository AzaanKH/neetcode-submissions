# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # count = 1
        # if root.right:
        #     count = max(self.maxDepth(root.right) + 1, count)

        # if root.left:
        #     count = max(self.maxDepth(root.left) + 1, count)
        q = deque()
        q.append(root)
        count = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count += 1
        return count