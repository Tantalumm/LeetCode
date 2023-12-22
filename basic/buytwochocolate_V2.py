class Solution:
    def buyChoco(prices: list[int], money: int) -> int:
        purchase = []
        for i in range(2):
            pos = prices.index(min(prices))
            purchase.append(prices.pop(pos))
        x = sum(purchase) 
        return money - x if money >= x else money 
                
p = [98,54,6,34,66,63,52,39]
#p = [1,2,2]
m = 62
print(Solution.buyChoco(p,m))