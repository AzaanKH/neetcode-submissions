class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key in count:
            heap.append((-count[key], key))
        heapq.heapify(heap)
        res = []
        while k > 0:
            _, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        return res