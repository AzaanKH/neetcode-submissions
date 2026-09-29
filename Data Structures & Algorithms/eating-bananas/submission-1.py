class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high:
            mid = (high + low) // 2
            count = 0
            i = 0
            temp = piles
            while i < len(piles):
                count += (piles[i] + mid - 1) // mid
                if count > h:
                    left = mid + 1
                i += 1
            if count <= h:
                res = min(mid, res)
                high = mid - 1
            else:
                low = mid + 1
        return res 
        