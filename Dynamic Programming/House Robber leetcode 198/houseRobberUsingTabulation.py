class Solution:
    def solve(self,index,nums,dp):
        m=len(nums)
        dp[0]=nums[0]
        for index in range(1,m):
            if index>1:
                pick=nums[index]+dp[index-2]
            else:
                pick=nums[index]
            notPick=0+dp[index-1]
            dp[index]=max(pick,notPick)
        return dp[index]
    def houseRobber(self,nums):
        n=len(nums)
        dp=[-1]*n
        return self.solve(n-1,nums,dp)
obj=Solution()
nums = [1,2,3,1]
print(obj.houseRobber(nums))