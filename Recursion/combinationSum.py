def solve(index,total,subset,nums,target,result):
    if total==target:
        result.append(subset[:])
        return
    elif total>target or index==len(nums):
        return
    sum=total+nums[index]
    subset.append(nums[index])
    solve(index+1,sum,subset,nums,target,result)
    sum=total
    subset.pop()
    solve(index+1,sum,subset,nums,target,result)
def combinationSum(nums,target):
    result=[]
    solve(0,0,[],nums,target,result)
    return result
print(combinationSum([0,1,2,3,4,5,6,7,8,9],6))