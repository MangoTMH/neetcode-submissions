class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            lowest = min(self.minStack[-1], val)
            self.minStack.append(lowest)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()        

    def top(self) -> int:
        x = self.stack[-1]
        return x

    def getMin(self) -> int:
        return self.minStack[-1]