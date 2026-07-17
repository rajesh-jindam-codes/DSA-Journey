nums=[1,2,3,0]
result=[]
k=2
exist=False
def solve(index,total,subset):
    if total==k:
        result.append(subset[:])
        global exist
        exist=True
        return 
    elif total>k or index==len(nums):
        return 
    subset.append(nums[index])
    sum=total+nums[index]
    solve(index+1,sum,subset)
    e=subset.pop()
    sum-=e
    solve(index+1,sum,subset)
solve(0,0,[])
print(result)
print(exist)