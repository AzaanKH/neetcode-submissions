class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if no rotten fruit impossible
        # otherwise run bfs for every level increase the min

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                visit.add((r, c))
                for nr, nc in neighbors:
                    newRow, newCol = r + nr, c + nc
                    if min(newRow, newCol) < 0 or newRow >= ROWS or newCol >= COLS or grid[newRow][newCol] != 1 or (newRow, newCol) in visit:
                        continue
                    q.append((newRow, newCol))
                    grid[newRow][newCol] = 2
                    fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1

        