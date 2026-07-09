prices=[0,2,4,5,9,45,0,90]
n=len(prices)
maxProfit=float('-inf')
minPrice=float('inf')
for i in range(n):
    minPrice=min(minPrice,prices[i])
    maxProfit=max(maxProfit,prices[i]-minPrice)
print(maxProfit)