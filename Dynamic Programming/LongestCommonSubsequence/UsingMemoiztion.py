class Solution:
    def solve(self,index1,index2,text1,text2,dp):
        if index1<0 or index2<0:
            return 0
        if dp[index1][index2]!=-1:
            return dp[index1][index2]   
        if text1[index1]==text2[index2]:
            dp[index1][index2] = 1+self.solve(index1-1,index2-1,text1,text2,dp)
        else:
            dp[index1][index2] = 0+max(self.solve(index1-1,index2,text1,text2,dp),self.solve(index1,index2-1,text1,text2,dp))
        return dp[index1][index2]
    def longestCommonSubsequense(self,text1,text2):
        dp=[[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.solve(len(text1)-1,len(text2)-1,text1,text2,dp)
obj=Solution()
print(obj.longestCommonSubsequense("abcde","ace"))