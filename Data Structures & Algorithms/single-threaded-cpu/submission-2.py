class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # use heap with start time, index and time needed
        heap = []
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x: x[0])
        N = len(tasks)
        time = tasks[0][0]
        res = []
        start = 0
        while len(res) != len(tasks):
            while start < N and tasks[start][0] <= time:
                heapq.heappush(heap, (tasks[start][1], tasks[start][2]))
                start += 1
            if not heap:
                time = tasks[start][0]
                continue
            if heap:
                update_time, index = heapq.heappop(heap)
                res.append(index)
                time += update_time
        return res