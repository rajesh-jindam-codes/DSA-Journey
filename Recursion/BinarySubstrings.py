def solve(index,flag,numbers,result):
    if index==len(numbers):
        result.append(''.join(numbers))
        return
    
    numbers[index]='0'
    solve(index+1,True,numbers,result)
    if flag==True:
        numbers[index]='1'
        solve(index+1,False,numbers,result)
        numbers[index]='0'

def binaryNumbers(n):
    numbers=['0']*(n)
    result=[]
    solve(0,True,numbers,result)
    return result
print(binaryNumbers(3))