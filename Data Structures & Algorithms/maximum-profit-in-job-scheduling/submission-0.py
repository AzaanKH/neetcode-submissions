import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        N = len(startTime)
        for i in range(N):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs = sorted(jobs, key=lambda x : x[0])

        cache = {}
        def dfs(i):
            if i >= N:
                return 0
            if i in cache:
                return cache[i]
            res = dfs(i + 1)
            end = jobs[i][1]
            j = bisect.bisect(jobs, (end, -1, -1)) 
            res = max(jobs[i][2] + dfs(j), res)
            cache[i] = res
            return res
        return dfs(0)

            

        