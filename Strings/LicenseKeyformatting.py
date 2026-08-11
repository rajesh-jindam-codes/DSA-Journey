class Solution:
    def licenseKeyFormatting(self,s,k):
        s=s.replace("-",'').upper()
        res=[]
        for i in range(len(s)-1,-1,-1):
            res.append(s[i])
            if (len(s)-1+1-i)%k==0 and i!=0:
                res.append("-")
        return ''.join(res[::-1])
s = "5F3Z-2e-9-w"
k = 4
obj=Solution()
print(obj.licenseKeyFormatting(s,k))