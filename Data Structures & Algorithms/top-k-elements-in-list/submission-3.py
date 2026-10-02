class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k freq elemets, use Counter to get element -> freq
        # have heap of size k and go through counter, when heap == k pop from heap

        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for key in count:
            freq[count[key]].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res