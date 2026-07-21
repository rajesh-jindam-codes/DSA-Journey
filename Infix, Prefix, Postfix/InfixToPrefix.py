def precedence(ch):
    if ch=='+' or ch=='-':
        return 1
    if ch=='*' or ch=='/':
        return 2
    if ch=='^':
        return 3
    return 0
def infixToPrefix(s):
    s=s[::-1]
    stack=[]
    result=[]
    s=s.replace('(','temp').replace(')','(').replace('temp',')')
    for char in s:
        if ('a'<=char<='z') or ("A"<=char<'Z') or ('0'<=char<='9'):
            result.append(char)
        elif char=='(':
            stack.append(char)
        elif char==')':
            while stack and stack[-1]!='(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1])>precedence(char):
                result.append(stack.pop())
            stack.append(char)
    while stack:
        result.append(stack.pop())
    return "".join(result[::-1])
print(infixToPrefix("(A+B-C)^D-E/F"))