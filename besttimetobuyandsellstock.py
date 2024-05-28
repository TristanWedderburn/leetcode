class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, buy_index, sell_index = 0, 0, 1

        while(sell_index < len(prices)): # move sell to find best price to sell at
            if (prices[buy_index] < prices[sell_index]): # if profitable, check
                max_profit = max(max_profit, prices[sell_index] - prices[buy_index])
            else: # move the buy index to lower price
                buy_index = sell_index
            sell_index+=1 # check next sell date

        return max_profit
