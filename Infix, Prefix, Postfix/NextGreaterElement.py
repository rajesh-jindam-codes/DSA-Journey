def nextGreater(nums):
    n=len(nums)
    result=[-1]*n
    stack=[]
    for i in range(n-1,-1,-1):
        while len(stack)!=0 and stack[-1]<=nums[i]:
            stack.pop()
        if len(stack)!=0:
            result[i]=stack[-1]
        stack.append(nums[i])
    return result
print(nextGreater([7,9,8,4,6,5,8,1,9,3,2,0,1,5]))