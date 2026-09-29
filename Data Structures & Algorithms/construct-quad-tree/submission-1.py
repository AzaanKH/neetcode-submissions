"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(rows, cols, size):
            start = grid[rows][cols]
            all_same = True
            for r in range(rows, rows + size):
                for c in range(cols, cols + size):
                    if grid[r][c] != start:
                        all_same = False
                        break
            if all_same:
                return Node(start, True)
            new_size = size // 2
            return Node(start, False,
            dfs(rows, cols, new_size),
            dfs(rows, cols + new_size, new_size),
            dfs(rows + new_size, cols, new_size),
            dfs(rows + new_size, cols + new_size, new_size))
        return dfs(0, 0, len(grid))