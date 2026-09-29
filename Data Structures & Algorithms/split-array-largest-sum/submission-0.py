class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        res = right
        def check(max_sum: int):
            groups = 1
            count = 0
            for n in nums:
                if count + n > max_sum:
                    groups += 1
                    count = n
                else:
                    count += n
            return groups <= k

        while left <= right:
            mid = (right + left) // 2
            if check(mid) == True:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
