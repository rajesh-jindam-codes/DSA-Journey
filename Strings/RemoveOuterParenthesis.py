class Solution:
    def removeOutermostParenthesis(self,s):
        count=0
        res=''
        for ch in s:
            if ch=='(':
                count+=1
                if count>1:
                    res+=ch 
            else:
                count-=1
                if count>0:
                    res+=ch
        return res
obj=Solution()
print(obj.removeOutermostParenthesis('(()())(())'))

            