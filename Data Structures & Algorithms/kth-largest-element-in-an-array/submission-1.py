class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        
        heap = [-n for n in nums]
        heapq.heapify(heap)

        while k != 1:
            heapq.heappop(heap)
            k -= 1
        return -1 * heap[0]