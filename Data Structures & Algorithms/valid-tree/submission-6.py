class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        find_x, find_y = self.find(x), self.find(y)
        if find_x == find_y:
            return False
        if self.rank[find_x] > self.rank[find_y]:
            self.parent[find_y] = find_x
        elif self.rank[find_x] < self.rank[find_y]:
            self.parent[find_x] = find_y
        else:
            self.parent[find_y] = find_x
            self.rank[find_x] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)
        for e1, e2 in edges:
            if not uf.union(e1, e2):
                return False
        return True