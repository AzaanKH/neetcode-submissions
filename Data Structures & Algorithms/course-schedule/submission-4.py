class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = {}
        in_degree = [0] * numCourses
        for pre, crs in prerequisites:
            in_degree[pre] += 1
            if crs not in course:
                course[crs] = []
            course[crs].append(pre)
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        visit = 0
        while q:
            node = q.popleft()
            visit += 1
            for next_course in course.get(node, []):
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        return visit == numCourses