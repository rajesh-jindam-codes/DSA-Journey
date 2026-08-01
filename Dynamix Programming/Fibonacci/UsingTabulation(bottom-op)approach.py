def fibonacci(num,dp):
    dp[0]=0
    dp[1]=1
    for i in range(2,num+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[num]
num=5
dp=[-1]*(num+1)
print(fibonacci(num,dp))