class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        visit.add((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visit.add((r, c))
            count = 0
            for dirRow, dirCol in directions:
                newRow, newCol = r + dirRow, c + dirCol
                if 0 <= newRow < ROWS and 0 <= newCol < COLS and (newRow, newCol) not in visit and grid[newRow][newCol] == 0:
                    count += dfs(newRow, newCol)
            visit.remove((r, c))
            return count
        
        return dfs(0, 0)
            