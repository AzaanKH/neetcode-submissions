class FreqStack:

    def __init__(self):
        self.map = {}
        self.max_count = 0
        self.val_freq = {}

    def push(self, val: int) -> None:
        freq = self.val_freq.get(val, 0)
        freq += 1
        self.val_freq[val] = freq
        if freq not in self.map:
            self.map[freq] = []
        self.map[freq].append(val)
        self.max_count = max(self.max_count, freq)
    def pop(self) -> int:
        x = self.map[self.max_count].pop()
        self.val_freq[x] -= 1
        if not self.map[self.max_count]:
            self.max_count -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()