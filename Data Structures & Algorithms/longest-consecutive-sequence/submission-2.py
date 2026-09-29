class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                seq = 0
                while n in nums:
                    seq += 1
                    n += 1
                res = max(seq, res)
        return res