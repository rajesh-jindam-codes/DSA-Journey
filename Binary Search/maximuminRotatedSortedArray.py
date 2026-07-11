nums=[4,5,6,7,8,9,20,1,2,3]
low=0
high=len(nums)-1
maximum=float('-inf')
while low<=high:
    mid=(low+high)//2
    maximum=max(nums[mid],maximum)
    if nums[mid]>=nums[low]:
        low=mid+1
    else:
        high=mid-1
print(maximum)