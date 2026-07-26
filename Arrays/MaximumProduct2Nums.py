class Solution:
    def maxProduct(self,n):
        first=0
        second=0
        while n>0:
            digit=n%10
            if digit>=first:
                second=first
                first=digit
            elif digit>second:
                second=digit
            n//=10
        return first*second
obj=Solution()
print(obj.maxProduct(9654289))