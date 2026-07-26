nums=[0,1,2,3,4,5,6,7,8,9]
def function(nums,left,right):
    while left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    return function(nums,left+1,right-1)
function(nums,0,len(nums)-1)
print(nums)
