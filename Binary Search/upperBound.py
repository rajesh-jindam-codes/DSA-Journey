nums= [-1,0,1,3,4,5,6,7,9]
n=len(nums)
low=0
target=3
high=n-1
ub=n
while low<=high:
    mid=(low+high)//2
    if nums[mid]>target:
        ub=mid
        high=mid-1
    else:
        low=mid+1
print(ub)