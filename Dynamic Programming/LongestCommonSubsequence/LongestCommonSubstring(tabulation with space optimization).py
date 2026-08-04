class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        prev= [0 for _ in range(m + 1)]
        maxi=0
        for i in range(1, m + 1):
            curr= [0 for _ in range(m + 1)]
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                    maxi=max(maxi,curr[j])
                else:
                    curr[j] = 0
            prev = curr
        return maxi 
                    
obj = Solution()
print(obj.longestCommonSubsequence("abcde", "abcpq"))  # Output: