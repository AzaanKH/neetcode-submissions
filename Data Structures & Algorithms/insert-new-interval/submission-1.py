class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        added = False
        for interval in intervals:
            start, end = interval
            if end < newInterval[0]:
                res.append(interval)
            elif start <= newInterval[1]:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
            elif start > newInterval[1]:
                if added == False:
                    res.append(newInterval)
                    added = True
                res.append(interval)
        if not added:
            res.append(newInterval)
        return res