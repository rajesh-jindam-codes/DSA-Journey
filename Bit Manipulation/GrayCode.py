class Solution:
    def grayCode(self,n):
        result=[]
        for i in range(2**n):
            gray=i^(i>>1)
            result.append(gray)
        return result
obj=Solution()
print(obj.grayCode(6))