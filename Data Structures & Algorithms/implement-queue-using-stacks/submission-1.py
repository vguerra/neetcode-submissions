class MyQueue:

    def __init__(self):
        self.stack = []
        self.rstack = []

    def push(self, x: int) -> None:
        if self.rstack:
            while self.rstack:
                self.stack.append(self.rstack.pop(-1))
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            while self.stack:
                self.rstack.append(self.stack.pop(-1))
        return self.rstack.pop(-1)

    def peek(self) -> int:
        if self.stack:
            while self.stack:
                self.rstack.append(self.stack.pop(-1))
        return self.rstack[-1]
        
    def empty(self) -> bool:
        return not self.stack and not self.rstack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


