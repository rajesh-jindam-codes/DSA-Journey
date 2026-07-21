def asteroidCollision(nums):
    n=len(nums)
    stack=[]
    for i in range(n):
        if nums[i]>0:
            stack.append(nums[i])
        else:
            while stack and stack[-1]<abs(nums[i]):
                stack.pop()
            if stack and stack[-1]==abs(nums[i]):
                stack.pop()
            elif not stack and stack[-1]<0:
                stack.append(nums[i])
    return stack
print(asteroidCollision([7,8,6,4,5,9,-9,-8,-6,-7,10]))