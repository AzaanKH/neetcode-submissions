class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        check = {0: -1}

        prefixSum = 0
        for i, n in enumerate(nums):
            prefixSum += n
            reaminder = prefixSum % k

            if reaminder in check:
                if i - check[reaminder] >= 2:
                    return True
            else:
                check[reaminder] = i
        return False

