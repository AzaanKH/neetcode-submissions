class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            temp = self.stack.pop()
        if temp == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
