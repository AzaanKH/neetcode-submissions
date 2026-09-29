class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        if fresh == 0:
            return 0
        minute = 0
        while q:
            minute += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        fresh -= 1
                        grid[nr][nc] = 2
                if fresh == 0:
                    return minute

        return minute if fresh == 0 else -1