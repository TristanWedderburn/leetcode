class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        buy=0
        sell=0
        i=0
        
        while(i < len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                sell = i
            while(i< len(prices) and i > buy and prices[i] >= prices[sell]):
                sell=i
                i+=1
            if sell > buy:
                profit+=(prices[sell]-prices[buy])
                buy = i
                sell = i
            i+=1
        
        return profit
