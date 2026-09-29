class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        i, j = 0, 0
        N, M = len(v1), len(v2)
        self.v = []
        start = True
        while i < N and j < M:
            if start:
                self.v.append(v1[i])
                i += 1
            else:
                self.v.append(v2[j])
                j += 1
            start = not start
        while i < N:
            self.v.append(v1[i])
            i += 1
        while j < M:
            self.v.append(v2[j])
            j += 1
        self.i = 0

    def next(self) -> int:
        current = self.v[self.i]
        self.i += 1
        return current
        

    def hasNext(self) -> bool:
        return self.i < len(self.v)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
