class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        pop = self.data.pop()
        if pop == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
