class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.max_freq = 0
        self.val_freq = {}

    def push(self, val: int) -> None:
        freq = self.val_freq.get(val, 0)
        freq += 1
        self.val_freq[val] = freq
        if freq not in self.stacks:
            self.stacks[freq] = []
        self.stacks[freq].append(val)
        self.max_freq = max(self.max_freq, freq)
    def pop(self) -> int:
        x = self.stacks[self.max_freq].pop()
        self.val_freq[x] -= 1
        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()