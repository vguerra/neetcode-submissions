class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            match tok:
                case '+':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op1 + op2)
                case '-':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 - op1)
                case '*':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op1 * op2)
                case '/':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(int(op2 / op1))
                case _:
                    stack.append(int(tok))
        return stack[0]

        