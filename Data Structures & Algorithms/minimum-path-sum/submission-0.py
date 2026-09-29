class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    dp[r][c] = grid[r][c]
                elif r == ROWS - 1:
                    dp[r][c] = grid[r][c] + dp[r][c + 1]
                elif c == COLS - 1:
                    dp[r][c] = grid[r][c] + dp[r + 1][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]