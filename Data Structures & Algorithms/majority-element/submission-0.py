class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, freq = 0, 0
        for i, n in enumerate(nums):
            if freq == 0:
                num = n
                freq = 1
            elif n != num:
                freq -= 1
            elif n == num:
                freq += 1
        return num