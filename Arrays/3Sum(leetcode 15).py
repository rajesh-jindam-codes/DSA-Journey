nums=[0,1,3,-1,-2,-3,5,4,6,3,2,6]
def threeSum(nums):
    res=[]
    nums.sort()
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total<0:
                left+=1
            elif total>0:
                right-=1
            else:
                res.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1

                while left<=right and nums[left]==nums[left-1]:
                    left+=1
                while left<=right and nums[right]==nums[right+1]:
                    right-=1
        return res
print(threeSum(nums))