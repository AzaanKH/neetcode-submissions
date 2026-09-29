class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x1, y1 = self.find(x), self.find(y)
        if x1 == y1:
            return False
        if self.rank[x1] >= self.rank[y1]:
            self.parent[y1] = x1
            self.rank[x1] += self.rank[y1]
        else:
            self.parent[x1] = y1
            self.rank[y1] += self.rank[x1]
        return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for e1, e2 in edges:
            if not uf.union(e1, e2):
                return [e1, e2]
        return []