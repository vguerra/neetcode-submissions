class MyStack:

    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
        

    def push(self, x: int) -> None:
        if self.queue1:
            self.queue1.append(x)
            return
        self.queue2.append(x)

    def pop(self) -> int:
        if self.queue1:
            n = len(self.queue1)
            for _ in range(n - 1):
                self.queue2.append(self.queue1.popleft())
            return self.queue1.popleft()
        else:
            n = len(self.queue2)
            for _ in range(n - 1):
                self.queue1.append(self.queue2.popleft())
            return self.queue2.popleft()

    def top(self) -> int:
        if self.queue1:
            return self.queue1[-1]
        return self.queue2[-1]        

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
