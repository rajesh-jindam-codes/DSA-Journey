nums=[5,2,1,0,0,4,1,5]
def jumpGame(nums):
    n=len(nums)
    maxIndex=0
    for i in range(n):
        if i>maxIndex:
            return False
        maxIndex=max(maxIndex,i+nums[i])
    return True
print(jumpGame(nums))