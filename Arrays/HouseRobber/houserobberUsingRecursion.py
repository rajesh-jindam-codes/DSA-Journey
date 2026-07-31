class Solution:
    def solve(self,index,nums):
        if index==0:
            return nums[index]
        if index<0:
            return 0
        pick=nums[index]+self.solve(index-2,nums)
        notPick=0+self.solve(index-1,nums)
        return max(pick,notPick)
    def houseRobber(self,nums):
        n=len(nums)
        return self.solve(n-1,nums)
obj=Solution()
nums = [1,2,3,1]
print(obj.houseRobber(nums))