nums=[5,2,1,0,0,4,1,5]
def jumpGame(index,jump,nums):
<<<<<<< HEAD
    if index>=len(nums)-1:
        return jump
    minJump=float('inf')
    for i in range(1,nums[index]+1):
        minJump=min(minJump,jumpGame(index+i,jump+1,nums))
    return minJump
print(jumpGame(0,0,nums))
=======
    n=len(nums)
    jumps=0
    left=0
    right=0
    while right<n-1:
        farthest=0
        for i in range(left,right+1):
            farthest=max(farthest,i+nums[i])
        left=right+1
        right=farthest
        jumps+=1
    return jumps
print(jumpGame(0,0,nums))
>>>>>>> 79cb04b (Jump Game 2 leetcode 45)
