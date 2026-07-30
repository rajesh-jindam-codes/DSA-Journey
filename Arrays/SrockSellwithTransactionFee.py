class Solution:
    def maxProfit(self,prices,fee):
        hold=-prices[0]
        cash=0
        for price in prices[1:]:
            hold=max(hold,cash-price)
            cash=max(cash,hold+price-fee)
        return cash
obj=Solution()
print(obj.maxProfit([5,6,3,1,4,2,4,8,1],2))