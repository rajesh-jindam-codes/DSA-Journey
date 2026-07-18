def solve(index,subset,target,result,nums):
    if target==0:
        result.add(tuple(subset[:]))
        return
    if target<0 or index==len(nums):
        return
    subset.append(nums[index])
    target-=nums[index]
    solve(index+1,subset,target,result,nums)
    subset.pop()
    target+=nums[index]
    solve(index+1,subset,target,result,nums)
def combinationSum(nums,target):
    result=set()
    nums.sort()
    solve(0,[],target, result, nums)
    return list(result)
print(combinationSum([0,1,2,3,4,5,6,7,8,9],6))