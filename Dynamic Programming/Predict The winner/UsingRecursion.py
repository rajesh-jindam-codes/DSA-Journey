class Solution:
    def solve(self,i,j,nums):
        if i==j:
            return nums[i]
        pickLeft=nums[i]-self.solve(i+1,j,nums)
        pickRight=nums[j]-self.solve(i,j-1,nums)
        return max(pickLeft,pickRight)
    def predictWinner(self,nums):
        return self.solve(0,len(nums)-1,nums)>=0
obj=Solution()
print(obj.predictWinner([1,5,2]))