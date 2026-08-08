def backtrack(nums,temp,used,ans):
    if len(temp)==len(nums):
        ans.append(temp[:])
        return
    for i in range(len(nums)):
        if used[i]==1:
            continue
        used[i]=1
        temp.append(nums[i])
        backtrack(nums,temp,used,ans)
        used[i]=0
        temp.pop()
def permutations(nums):
    used=[0]*len(nums)
    ans=[]
    backtrack(nums,[],used,ans)
    return ans
nums=[1,2,3]
print(permutations(nums))