class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        cache = {}
        def dfs(start, i, take):
            if start >= N:
                return 0
            if (start, i, take) in cache:
                return cache[(start, i, take)]
            res = 0 if take else float("inf")
            total = 0
            for x in range(1, 2 * i + 1):
                if start + x > N:
                    break
                total += piles[start + x - 1]
                if take:
                    res = max(total + dfs(start + x, max(i, x), not take), res)
                else:
                    res = min(dfs(start + x, max(i, x), not take), res)
            cache[(start, i, take)] = res
            return res
        return dfs(0, 1, True)