class Solution:
    def solve(self,index1,index2,text1,text2):
        if index1<0 or index2<0:
            return 0
        if text1[index1]==text2[index2]:
            return 1+self.solve(index1-1,index2-1,text1,text2)
        return 0+max(self.solve(index1-1,index2,text1,text2),self.solve(index1,index2-1,text1,text2))
    def longestCommonSubsequense(self,text1,text2):
        return self.solve(len(text1)-1,len(text2)-1,text1,text2)
obj=Solution()
print(obj.longestCommonSubsequense("abcde","ace"))