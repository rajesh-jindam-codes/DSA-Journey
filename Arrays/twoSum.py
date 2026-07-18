nums=[5,0,1,6,2,7,9,1,8]
def twoSum(nums,target):
    n=len(nums)
    seen={}
    for i in range(n):
        compliment =target-nums[i]
        if compliment in seen:
            return [seen[compliment],i]
        seen[nums[i]]=i
print(twoSum(nums,9))
