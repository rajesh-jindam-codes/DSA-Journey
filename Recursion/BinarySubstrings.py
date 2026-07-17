def solve(index,total,brackets,result,n):
    if index==2*n:
        if total==0:
            result.append("".join(brackets))
        return
    if total>n or total<0:
        return 
    brackets[index]='('
    solve(index+1,total+1,brackets,result,n)
    brackets[index]=')'
    solve(index+1,total-1,brackets,result,n)
def paranthesis(n):
    brackets=[""]*(2*n)
    result=[]
    solve(0,0,brackets,result,n)
    return result
n=3
print(paranthesis(n))