class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        q = deque()
        if grid[0][0] == 1:
            return -1
        q.append((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0
        while q:
            
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return count
                visit.add((r, c))
                for dirRow, dirCol in directions:
                    newRow, newCol = r + dirRow, c + dirCol
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and (newRow, newCol) not in visit and grid[newRow][newCol] == 0:
                        q.append((newRow, newCol))
            count += 1
        return -1