
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            even = True if (r - l) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            cache[(l, r)] = max(left + dfs(l + 1, r), right + dfs(l, r - 1)) 
            return cache[(l, r)]
        return dfs(0, len(piles) - 1) > sum(piles) // 2
