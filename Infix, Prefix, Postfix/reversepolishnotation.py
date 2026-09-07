class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                b=stack.pop()
                a=stack.pop()
                if token=='+':
                    stack.append(a+b)
                elif token =='-':
                    stack.append(a-b)
                elif token=='*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[-1]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))