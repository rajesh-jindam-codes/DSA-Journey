def longestOnes(nums,k):
    maxLen=0
    left=0
    right=0
    zeroes=0
    n=len(nums)
    while right<n:
        if nums[right]==0:
            zeroes+=1
        if zeroes>k:
            if nums[left]==0:
                zeroes-=1
            left+=1
        if zeroes<=k:
            length=right-left+1
            maxLen=max(maxLen,length)
        right+=1
    return maxLen
print(longestOnes([0,1,0,1,1,1,1,0,0,0,0,1],2))