class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [0] * N
        suffix = [0] * N
        currentSum = 1
        for i, n in enumerate(nums):
            prefix[i] = currentSum
            currentSum *= n
        currentSum = 1
        for i in range(N - 1, -1, -1):
            suffix[i] = currentSum
            currentSum *= nums[i]
        res = []
        for i in range(N):
            res.append(prefix[i] * suffix[i])
        return res