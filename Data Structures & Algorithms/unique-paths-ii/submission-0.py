class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0] * (COLS + 1)
        prevRow[COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            currentRow = [0] * (COLS + 1)
            for c in range(COLS  - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    currentRow[c] = 0
                else:
                    currentRow[c] = currentRow[c + 1] + prevRow[c]
            prevRow = currentRow
        return prevRow[0]