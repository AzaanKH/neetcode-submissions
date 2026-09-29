class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visit = set()
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            count = 1
            for nr, nc in neighbors:
                newRow, newCol = r + nr, c + nc
                count += dfs(newRow, newCol)
            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, dfs(r, c))
        return res