class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force try all possible scenarios might TLE
        # can possbliy use prefix sum some how
        res = curr = 0
        prefix = {0 : 1}
        for n in nums:
            curr += n
            target = curr - k
            res += prefix.get(target, 0)
            prefix[curr] = prefix.get(curr, 0) + 1
        return res 