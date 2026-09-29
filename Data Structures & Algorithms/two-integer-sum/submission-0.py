class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in check:
                return [check[compliment], i]
            check[n] = i
        return []
        