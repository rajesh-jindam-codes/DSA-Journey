class Solution:
    def solve(self,num,dp):
        if num==0:
            return 0
        if num==1:
            return 1
        if dp[num]!=-1:
            return dp[num]
        dp[num]=self.fibonacci(num-1)+self.fibonacci(num-2)
        return dp[num]
    def fibonacci(self,num):
        dp=[-1]*(num+1)
        return self.solve(num,dp)
obj=Solution()
print(obj.fibonacci(10))