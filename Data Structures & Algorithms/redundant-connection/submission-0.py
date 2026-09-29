class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_y] > self.rank[root_x]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # UnionFind on each edge and if the edge already exists then return it
        start = UnionFind(len(edges))
        for x, y in edges:
            if start.union(x, y) == False:
                return [x, y]
        return []