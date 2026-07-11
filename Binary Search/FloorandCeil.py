nums = [0,2,4,6,8,10,12]
floor=-1
ceil=-1
n=len(nums)
target=11
for i in range(n):
    if nums[i]==target:
        floor=nums[i]
        ceil=nums[i]
        break
    elif nums[i]>target:
        ceil=nums[i]
        if i>0:
            floor= nums[i-1]
        break
    if target>nums[n-1]:
        floor=nums[n-1]
        ceil-=1
print(ceil)
print(floor)