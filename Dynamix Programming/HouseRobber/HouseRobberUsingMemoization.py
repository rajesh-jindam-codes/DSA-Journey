class Solution:
    def solve(self,index,nums,dp):
        if index==0:
            return nums[index]
        if index<0:
            return 0
        if dp[index]!=-1:
            return dp[index]
        pick=nums[index]+self.solve(index-2,nums,dp)
        notPick=0+self.solve(index-1,nums,dp)
        dp[index]=max(pick,notPick)
        return dp[index]
    def houseRobber(self,nums):
        n=len(nums)
        dp=[-1]*n
        return self.solve(n-1,nums,dp)
obj=Solution()
nums = [1,2,3,1]
print(obj.houseRobber(nums))