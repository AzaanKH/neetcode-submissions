class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0' or (r, c) in visit:
                return
            visit.add((r, c))

            for newRow, newCol in neighbors:
                
                dfs(r + newRow, c + newCol)
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    res += 1
                    dfs(r, c)
        return res