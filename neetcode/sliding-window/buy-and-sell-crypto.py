from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, profit = 0, 1, 0
        while r < len(prices):
            buy, sell = prices[l], prices[r]
            profit = max(profit, sell - buy)
            if buy > sell: l = r
            r += 1
        return profit

s = Solution()
prices = [10,1,5,6,7,1]
print("Prices: {}, Result: {}, Expected: 6".format(prices, s.maxProfit(prices)))

prices = [10,8,7,5,2]
print("Prices: {}, Result: {}, Expected: 0".format(prices, s.maxProfit(prices)))

prices = [5,1,5,6,7,1,10]
print("Prices: {}, Result: {}, Expected: 9".format(prices, s.maxProfit(prices)))

prices=[2,1,2,1,0,1,2]
print("Prices: {}, Result: {}, Expected: 2".format(prices, s.maxProfit(prices)))