class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                num = int(num1) + int(num2)
                stack.append(str(num))
            elif t == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                num = int(num2) - int(num1)
                stack.append(str(num))
            elif t == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                num = int(num1) * int(num2)
                stack.append(str(num))
            elif t == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                num = int(float(num2) / int(num1))
                stack.append(str(num))
            else:
                stack.append(t)
        return int(stack.pop())
            