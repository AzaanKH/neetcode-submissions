class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k freq elemets, use Counter to get element -> freq
        # have heap of size k and go through counter, when heap == k pop from heap

        count = Counter(nums)
        heap = []
        for key in count:
            heapq.heappush(heap, (count[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        

        res = []
        while heap:
            freq, val = heapq.heappop(heap)
            res.append(val)
        
        return res