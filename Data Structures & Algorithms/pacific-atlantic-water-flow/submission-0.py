class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, visit, prevHeight):
            if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, float("-inf"))
            dfs(ROWS - 1, c, atl, float("-inf"))
        
        for r in range(ROWS):
            dfs(r, 0, pac, float("-inf"))
            dfs(r, COLS - 1, atl, float("-inf"))

        res = []
        for r, c in atl:
            if (r, c) in pac:
                res.append([r, c])
        return res
