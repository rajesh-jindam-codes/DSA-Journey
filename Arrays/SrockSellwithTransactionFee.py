class Solution:
    def maxProfit(self,prices,fee):
        hold=-prices[0]
        cash=0
        for price in prices[1:]:
            hold=max(hold,cash-price)
            cash=max(cash,hold+price-fee)
        return cash
obj=Solution()
print(obj.maxProfit([5,1,3,6,4,2,0,7,8,9,4,0,10],3))