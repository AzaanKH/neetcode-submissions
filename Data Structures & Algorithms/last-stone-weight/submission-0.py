class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-w for w in stones]
        heapq.heapify(new_stones)

        while len(new_stones) > 1:
            x = heapq.heappop(new_stones)
            y = heapq.heappop(new_stones)
            if x != y:
                newStone = (x + (-1 * y))
                heapq.heappush(new_stones, newStone)

        return new_stones[0] * -1 if new_stones else 0
        