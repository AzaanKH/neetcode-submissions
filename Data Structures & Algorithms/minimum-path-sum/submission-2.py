class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        prevRow = [0] * (COLS + 1)
        for r in range(ROWS - 1, -1, -1):
            currentRow = [0] * (COLS + 1)
            for c in range(COLS - 1, -1, -1):
                if c == COLS - 1 and r == ROWS - 1:
                    currentRow[c] = grid[r][c]
                elif c == COLS - 1:
                    currentRow[c] = grid[r][c] + prevRow[c]
                elif r == ROWS - 1:
                    currentRow[c] = grid[r][c] + currentRow[c + 1]
                else:
                    currentRow[c] = grid[r][c] + min(currentRow[c + 1], prevRow[c])
                
            prevRow = currentRow
                
        # print(prevRow)
        return prevRow[0]