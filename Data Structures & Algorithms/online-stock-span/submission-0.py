class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        tmp = []
        count = 0
        while self.stack and self.stack[-1] <= price:
            tmp.append(self.stack.pop())
            count += 1
        while tmp:
            self.stack.append(tmp.pop())
        self.stack.append(price)

        return count + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)