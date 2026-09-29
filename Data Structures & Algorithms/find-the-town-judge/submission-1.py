class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # go through trust set up a defaultdict and see which person can be town find
        # then iterate through the dict again to check if everyon trusts the judge
        check = defaultdict(set)

        for ai, bi in trust:
            check[ai].add(bi)
        
        possible_mayors = []
        for i in range(n + 1):
            if i not in check:
                possible_mayors.append(i)

        for mayor in possible_mayors:
            can_mayor = True
            for key in check:
                if mayor not in check[key]:
                    can_mayor = False
                    break
            if can_mayor:
                return mayor
        return -1