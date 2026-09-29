class StockSpanner:

    def __init__(self):
        self.count = []

    def next(self, price: int) -> int:
        if not self.count:
            self.count.append(price)
            return 1
        R = len(self.count) - 1
        res = 0
        while R >= 0 and self.count[R] <= price:
            res += 1
            R -= 1
        self.count.append(price)
        return res + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)