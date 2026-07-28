nums=[4,5,6,7,-3,-1,-2,0,1,2,3]
low=0
high=len(nums)-1
minimum=float('inf')
while low<=high:
    mid=(low+high)//2
    if minimum>nums[mid]:
        minimum=nums[mid]
    if nums[mid]<nums[high]:
        high=mid-1
    else:
        low=mid+1
print(minimum)
