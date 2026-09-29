class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        res = deque()
        left = 0
        for r in range(len(arr)):
            if len(res) < k:
                res.append(arr[r])
            else:
                if abs(arr[r] - x) < abs(arr[left] - x):
                    res.popleft()
                    res.append(arr[r])
                    left += 1 
        return list(res)