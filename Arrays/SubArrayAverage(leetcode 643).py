def findMaxAverage(nums,k):
    n=len(nums)
    windowSum=sum(nums[:k])
    maxSum=windowSum
    for i in range(k,n):
        windowSum+=nums[i]-nums[i-k]
        maxSum=max(maxSum,windowSum)
    return maxSum/k
nums=[1,12,-5,-6,50,3]
k=3
print(findMaxAverage(nums,k))