class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
    
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
        elif self.rank[find_y] > self.rank[find_x]:
            self.parent[find_x] = find_y
        else:
            self.parent[find_y] = find_x
            self.rank[x] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = UnionFind(len(edges))

        for e1, e2 in edges:
            if not union.union(e1, e2):
                return [e1, e2]
        return []