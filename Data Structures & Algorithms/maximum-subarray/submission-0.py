class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        count = 0
        
        for n in nums:
            count += n
            if count <= 0:
                res = max(count, res)
                count = 0
                continue
            res = max(count, res)
        return res
        