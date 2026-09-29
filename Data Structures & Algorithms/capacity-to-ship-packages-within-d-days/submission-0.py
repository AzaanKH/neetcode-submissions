class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap):
            ships = 1
            current_cap = cap
            for w in weights:
                if current_cap - w < 0:
                    ships += 1
                    current_cap = cap
               
                if ships > days:
                    return False
                current_cap -= w
            return True
        left, right = max(weights), sum(weights)
        res = right
        while left <= right:
            mid = (left + right) // 2
            cap = can_ship(mid)
            if cap:
                res = min(mid, res)
                right = mid - 1
            else:
                left = mid + 1
        return res