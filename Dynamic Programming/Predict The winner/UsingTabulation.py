class SOlution:
    def predictWinner(self,nums):
        n=len(nums)
        dp=[[0 for _ in range(n)]for _ in range(n)]
        for i in range(n):
            dp[i][i]=nums[i]
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                pickLeft=nums[i]-dp[i+1][j]
                pickRight=nums[j]-dp[i][j-1]

                dp[i][j]=max(pickLeft,pickRight)
        return dp[0][n-1]>=0
obj=SOlution()
print(obj.predictWinner([1,5,2]))
