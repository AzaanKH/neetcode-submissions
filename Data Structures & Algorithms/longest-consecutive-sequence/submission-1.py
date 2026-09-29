class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        if not nums:
            return 0
        for n in nums:
            if n - 1 not in nums:
                count = n
                while count + 1 in nums:
                    count += 1
                res = max(count - n  + 1, res)
        return res if res > 0 else 1 