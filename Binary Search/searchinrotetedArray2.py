nums=[7,8,9,0,1,2,3,4,5,6]
found=False
target=15
low=0
high=len(nums)-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        found=True
    if nums[low]==nums[mid]==nums[high]:
        low+=1
        high-=1
        continue
    if nums[low]<=nums[mid]:
        if nums[low]<=target<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        if nums[mid]<target<=nums[high]:
            low=mid+1
        else:
            high=mid-1
print(found)