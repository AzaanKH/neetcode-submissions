class HitCounter:

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.clean_queue(timestamp)
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        self.clean_queue(timestamp)
        return len(self.queue)
    
    def clean_queue(self, timestamp: int) -> None:
        while self.queue and timestamp - 300 >= self.queue[0]:
            self.queue.popleft()
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
