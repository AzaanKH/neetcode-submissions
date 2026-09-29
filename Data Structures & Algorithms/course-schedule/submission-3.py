class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = defaultdict(list)
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj_list[pre].append(crs)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        visited_count = 0
        while q:
            crs = q.popleft()
            visited_count += 1
            for nextCrs in adj_list[crs]:
                indegree[nextCrs] -= 1

                if indegree[nextCrs] == 0:
                    q.append(nextCrs)
        return visited_count == numCourses