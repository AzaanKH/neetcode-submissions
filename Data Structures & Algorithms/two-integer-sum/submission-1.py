class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, n in enumerate(nums):
            if target - n in check:
                return [check[target - n], i]
            check[n] = i
        return None