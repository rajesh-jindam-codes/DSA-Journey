def posttopre(s):
    stack=[]
    n=len(s)
    for char in s:
        if char.isalnum():
            stack.append(char)
        else:
            operand1=stack.pop()
            operand2=stack.pop()
            newExpr=f'({char}{operand1}{operand2})'
            stack.append(newExpr)
    return stack[-1]
print(posttopre('DS*AG-/'))