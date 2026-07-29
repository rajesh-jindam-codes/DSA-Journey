class Solution:
    def findShortedtSubarray(self,nums):
        count={}
        first={}
        last={}
        for i,num in enumerate(nums):
            count[num]=count.get(num,0)+1
            if num not in first:
                first[num]=i
            last[num]=i
        degree=max(count.values())
        ans=len(nums)
        for num in count:
            if count[num]==degree:
                length=last[num]-first[num]+1
                ans=min(ans,length)
        return ans
obj=Solution()
nums = [1,2,2,3,1]
print(obj.findShortedtSubarray(nums))