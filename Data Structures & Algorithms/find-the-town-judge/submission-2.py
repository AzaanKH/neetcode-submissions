class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # go through trust set up a defaultdict and see which person can be town find
        # then iterate through the dict again to check if everyon trusts the judge
        check = [0] * (n + 1)
        for a, b in trust:
            check[a] -= 1
            check[b] += 1
        
        for i in range(1, n + 1):
            if check[i] == n - 1:
                return i
        return -1
        