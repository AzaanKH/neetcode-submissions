class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visit = set()
        heap = [(0, 0, 0)]
        res = 0
        ROWS, COLS = len(heights), len(heights[0])
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while heap:
            cost, r, c = heapq.heappop(heap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return cost
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visit or not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                temp_cost = max(abs(heights[r][c] - heights[nr][nc]), cost)
                heapq.heappush(heap, (temp_cost, nr, nc))


