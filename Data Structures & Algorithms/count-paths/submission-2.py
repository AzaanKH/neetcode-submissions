class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * (n + 1)
        prevRow[n - 1] = 1
        for r in range(m - 1, -1, -1):
            currentRow = [0] * (n + 1)
            for c in range(n - 1, -1, -1):
                currentRow[c] = prevRow[c] + currentRow[c + 1]
            prevRow = currentRow
        return prevRow[0]