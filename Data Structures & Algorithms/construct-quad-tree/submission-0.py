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
        # val True if 1 else False
        # 2d area -> Quad-Tree
        # if grid has same value isLeaf -> True val to value of grid, 4 children Null stop
        # if grid seperate values isLeaf False set val divide into 4 sub grids
        # recurse each children 
        # visit each grid value try to continously grow while setting the isLeaf and val
        # check if all values are the same
        
        def helper(r1, c1, size):
            all_same = True
            val = grid[r1][c1]
            for r in range(r1, r1 + size):
                for c in range(c1, c1 + size):
                    if grid[r][c] != val:
                        all_same = False
                        break
            if all_same:
                return Node(val == 1, True, None, None, None, None)
            half = size // 2
            return Node(
                True, False,
                helper(r1, c1, half),
                helper(r1, c1 + half, half),
                helper(r1 + half, c1, half),
                helper(r1 + half, c1 + half, half)
            )
        return helper(0, 0, len(grid))