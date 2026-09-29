class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        right = max(piles)
        left = 1

        while left <= right:
            mid = (left + right) // 2
            currentH = 0
            for p in piles:
                currentH += math.ceil(float(p) / mid)
                if currentH > h:
                    left = mid + 1
            if currentH <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

        