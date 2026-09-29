class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = deque()
        for v in [v1, v2]:
            if v:
                self.queue.append((v, 0))


    def next(self) -> int:
        vec, idx = self.queue.popleft()
        val = vec[idx]
        if idx + 1 < len(vec):
            self.queue.append((vec, idx + 1))
        return val



        
        

    def hasNext(self) -> bool:
        return bool(self.queue)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
