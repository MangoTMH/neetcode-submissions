class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()        

    def top(self) -> int:
        x = self.minStack[-1]
        return x

    def getMin(self) -> int:
        lowest = self.minStack[0]
        for i in self.minStack:
            if i < lowest:
                lowest = i
        return lowest