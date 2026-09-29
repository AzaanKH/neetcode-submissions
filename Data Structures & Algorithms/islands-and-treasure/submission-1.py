class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        # start nodes in bfs are 0, so there is no repeated work
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        # run bfs on the grid
        while q:
            for _ in range(len(q)):
                r, c, cost = q.popleft()
                cost += 1
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF):
                        grid[nr][nc] = cost
                        q.append((nr, nc, cost))
                        
