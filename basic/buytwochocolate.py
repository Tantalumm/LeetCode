##Version 1
class Solution:
    def buyChoco(prices: list[int], money: int) -> int:
        purchase = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i] + prices[j] <= money :
                    purchase.append((prices[i]+prices[j]))
        if purchase == [] :
            return money
        else : return money - min(purchase)
                
p = [98,54,6,34,66,63,52,39]
#p = [1,2,2]
m = 62            
print(Solution.buyChoco(p,m))

        