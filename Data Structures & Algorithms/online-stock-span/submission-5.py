class StockSpanner:

    def __init__(self):
        self.count = [] 
        # pair of price, span

    def next(self, price: int) -> int:
        span = 1
        while self.count and self.count[-1][0] <= price:
            span += self.count[-1][1]
            self.count.pop()
        self.count.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)