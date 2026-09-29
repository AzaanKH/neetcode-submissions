from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(l, r):
            if l > r:
                return 0
            even = True if (r - l) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            return max(left + dfs(l + 1, r), right + dfs(l, r - 1))
        return dfs(0, len(piles) - 1) > sum(piles) // 2
