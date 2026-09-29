class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(arrays)):
            res = max(abs(max(arrays[i]) - min(arrays[i - 1])), 
                        abs(min(arrays[i]) - max(arrays[i - 1])), 
                        res)

        return res