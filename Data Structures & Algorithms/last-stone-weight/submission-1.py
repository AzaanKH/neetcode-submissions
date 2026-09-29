class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max heap
        # run the simulation then return the weight of last stone if there is a last stone

        cost = [-x for x in stones]
        heapq.heapify(cost)

        while len(cost) > 1:
            x = heapq.heappop(cost)
            y = heapq.heappop(cost)
            if x != y:
                new_cost = x - y
                heapq.heappush(cost, new_cost)
        
        return (-1 * cost[0]) if cost else 0
        