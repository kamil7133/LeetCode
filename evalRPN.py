class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = ["+", "-", "*", "/"]
        eval_stack = []
        for i in tokens:
            try:
                num = int(i)
                eval_stack.append(num)
            except ValueError:
                b = eval_stack.pop()
                a = eval_stack.pop()
                if i == operators[0]:
                    eval_stack.append(a+b)
                elif i == operators[1]:
                    eval_stack.append(a-b)
                elif i == operators[2]:
                    eval_stack.append(a*b)
                elif i == operators[3]:
                    eval_stack.append(int(a / b))
        return eval_stack[-1]

#test
solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"]))
print(solution.evalRPN(["4","13","5","/","+"]))
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))