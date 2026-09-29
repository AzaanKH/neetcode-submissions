class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # for every land check all 4 sides, if you are out of bounds then increment boundry 
        # or if you are connected to water increment boundry
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    left = top = bottom = right = 0
                    if r == 0 or (grid[r - 1][c] == 0):
                        top = 1
                    if r == ROWS - 1 or grid[r + 1][c] == 0:
                        bottom = 1
                    if c == 0 or grid[r][c - 1] == 0:
                        left = 1
                    if c == COLS - 1 or grid[r][c + 1] == 0:
                        right = 1
                    res += (left + top + bottom + right)
        return res