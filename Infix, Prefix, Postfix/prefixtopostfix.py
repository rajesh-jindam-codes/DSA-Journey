def pretoppost(s):
    stack=[]
    n=len(s)
    for i in range(n-1,-1,-1):
        char=s[i]
        if char.isalnum():
            stack.append(char)
        else:
            operand1=stack.pop()
            operand2=stack.pop()
            newExpr=operand1+operand2+char
            stack.append(newExpr)
    return stack[-1]
print(pretoppost('/*DS-AG'))
