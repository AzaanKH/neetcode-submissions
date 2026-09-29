class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        check = set()
        for course, prev in prerequisites:
            adj_list[course].append(prev)
        
        def dfs(course):
            if course in check:
                return False
            if adj_list[course] == []:
                return True
            check.add(course)
            for next_course in adj_list[course]:
                if dfs(next_course) == False:
                    return False
            check.remove(course)
            adj_list[course] = []
            return True

        for n in range(numCourses):
            if dfs(n) == False:
                return False
        
        return True
        