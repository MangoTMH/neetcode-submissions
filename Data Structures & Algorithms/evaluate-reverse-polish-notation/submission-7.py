class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for i in tokens:
            if (i == "+"):
                second = stack.pop()
                first = stack.pop()
                res = first + second
                stack.append(res)

            elif (i == "-"):
                second = stack.pop()
                first = stack.pop()
                res = first - second
                stack.append(res)

            elif (i == "*"):
                second = stack.pop()
                first = stack.pop()
                res = first * second
                stack.append(res)

            elif (i == "/"):
                second = stack.pop()
                first = stack.pop()
                res = int(first / second)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack.pop()