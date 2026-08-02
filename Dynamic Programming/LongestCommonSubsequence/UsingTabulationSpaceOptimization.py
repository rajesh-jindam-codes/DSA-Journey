class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        prev=[0] * (n + 1)
        for ind2 in range(n+1):
            prev[ind2]=0
        for ind1 in range(1,m+1):
            curr=[0] * (n + 1)
            for ind2 in range(1,n+1):
                if text1[ind1-1]==text2[ind2-1]:
                    curr[ind2] = 1+prev[ind2-1]
                else:  
                    curr[ind2] = max(prev[ind2],curr[ind2-1])
            prev=curr
        return prev[n]
obj=Solution()
print(obj.longestCommonSubsequence("abcde", "ace"))  # Output: 3