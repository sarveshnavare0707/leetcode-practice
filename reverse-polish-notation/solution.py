'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.
'''

class Solution:
    def evalRPN(self, tokens):
        oplist = ["+","-","*","/"]
        op1 = None
        op2 = None
        stack = []
        for t in tokens:
            if t not in oplist:
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if t=='+':
                    stack.append(op1+op2)
                elif t=='-':
                    stack.append(op1-op2)
                elif t=='*':
                    stack.append(op1*op2)
                else:
                    stack.append(int(op1/op2))
        return stack.pop()

if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["2","1","+"])) # Output: 3
    print(s.evalRPN(["2","1","-"])) # Output: 1
    print(s.evalRPN(["4","13","5","/","+"])) # Output: 6
    print(s.evalRPN(["10","6","9","3","/","+","*"])) # Output: 90