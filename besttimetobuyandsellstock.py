class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force method would be to calculate max profit for each buy day i then return the max value
        if not prices or len(prices) <= 1:
            return 0
        
        buy = 0
        sell = 0
        profit = 0
        
        for day, price in enumerate(prices):
            if price < prices[buy]:
                buy = day
                sell = day
            if price > prices[sell]:
                sell = day
                profit = max(profit, prices[sell] - prices[buy])
            
        return profit
                
