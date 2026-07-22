nums=[7,2,1,0,0,4,1,5]
def jumpGame(index,jump,nums):
    if index>=len(nums)-1:
        return jump
    minJump=float('inf')
    for i in range(1,nums[index]+1):
        minJump=min(minJump,jumpGame(index+i,jump+1,nums))
    return minJump
print(jumpGame(0,0,nums))