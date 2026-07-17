nums=[1,2,3]
result=[]
def solve(index,subset):
    if index==len(nums):
        result.append(subset[:])
        return 
    subset.append(nums[index])
    solve(index+1,subset)
    subset.pop()
    solve(index+1,subset)
solve(0,[])
print(result)