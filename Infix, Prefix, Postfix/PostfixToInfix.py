def postfixtoInfix(s):
    stack=[]
    for char in s:
        if char.isalnum():
            stack.append(char)
        else:
            operand2=stack.pop()
            operand1=stack.pop()

            newExpr=f'({operand1}{char}{operand2})'
            stack.append(newExpr)

    return stack[-1]
print(postfixtoInfix('AB*C/D+F^'))
