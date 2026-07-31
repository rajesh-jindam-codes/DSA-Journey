class Solution:
    def issubSequence(self,s,t):
        i=j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
obj=Solution()
s = "abc"
t = "ahbgdc"
print(obj.issubSequence(s,t))