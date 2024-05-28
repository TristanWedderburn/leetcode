class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = prices[0]
        max_sell_price = 0
        max_profit = 0

        for i in range(len(prices)):
            if (prices[i] < min_buy_price): # new price to buy at
                min_buy_price = prices[i]
            elif prices[i] - min_buy_price > max_profit: # if more profitable, set
                max_sell_price = prices[i]
                max_profit = prices[i] - min_buy_price
        return max_profit
