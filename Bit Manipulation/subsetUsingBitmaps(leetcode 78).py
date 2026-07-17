def subset(nums):
    res=[]
    n=len(nums)
    for num in range(1<<n):
        subset=[]
        for i in range(n):
            if num &(1<<i)!=0:
                subset.append(nums[i])
        res.append(subset)
    return res
print(subset([1,2,3]))