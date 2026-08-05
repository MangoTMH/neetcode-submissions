class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()        

    def top(self) -> int:
        x = self.stack[-1]
        return x

    def getMin(self) -> int:
        lowest = self.stack[0]
        for i in self.stack:
            if i < lowest:
                lowest = i
        return lowest