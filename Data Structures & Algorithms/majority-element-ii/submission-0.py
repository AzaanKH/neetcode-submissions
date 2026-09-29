class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        size = N // 3
        count = Counter(nums)
        res = []
        print(size)
        for key in count:
            if count[key] > size:
                res.append(key)
        return res