nums=[1,2,2]
result=[]
def solve(index,nums,subset,result):
    if index>=len(nums):
        result.append(sum(subset))
        return
    subset.append(nums[index])
    solve(index+1,nums,subset,result)
    subset.pop()
    solve(index+1,nums,subset,result)
solve(0,nums,[],result)
print(result)