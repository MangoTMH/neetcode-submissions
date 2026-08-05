class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for i in tokens:
            if (i == "+"):
                second = int(stack.pop())
                first = int(stack.pop())
                res = first + second
                stack.append(res)

            elif (i == "-"):
                second = int(stack.pop())
                first = int(stack.pop())
                res = first - second
                stack.append(res)

            elif (i == "*"):
                second = int(stack.pop())
                first = int(stack.pop())
                res = first * second
                stack.append(res)

            elif (i == "/"):
                second = int(stack.pop())
                first = int(stack.pop())
                res = int(first / second)
                stack.append(res)
            else:
                stack.append(i)
        return int(stack.pop())