class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate all the points value
        # heap is points val and the index of points 
        # go through heap and get the k highest vals
        heap = []
        
        for i, point in enumerate(points):
            x, y = point
            distance = math.sqrt((x ** 2) + (y ** 2))
            # print(distance)
            heapq.heappush(heap, (distance, i))

        res = []
        
        while k != 0:
            _ , i = heapq.heappop(heap)
            res.append(points[i])
            k -= 1
        
        return res
        