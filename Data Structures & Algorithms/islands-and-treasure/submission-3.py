class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                cost = grid[r][c] + 1
                
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF):
                        grid[nr][nc] = cost
                        q.append((nr, nc))
        return