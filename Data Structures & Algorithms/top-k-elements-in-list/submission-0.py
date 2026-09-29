class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key in count:
            heapq.heappush(heap, (-count[key], -key))
        res = []
        while k > 0 and heap:
            count, i = heapq.heappop(heap)
            res.append(-i)
            k -= 1
        return res