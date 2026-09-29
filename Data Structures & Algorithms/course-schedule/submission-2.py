class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[v].append(u)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if adj_list[course] == []:
                return True
            visit.add(course)
            for nextCourse in adj_list[course]:
                if dfs(nextCourse) == False:
                    return False
            adj_list[course] = []
            visit.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True