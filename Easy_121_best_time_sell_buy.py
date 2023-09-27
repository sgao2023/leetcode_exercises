class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #The following uses the method of two pointers. Buy pointer and sell pointer. 
        buy=0
        sell=0
        profit=0
        max_profit=0
        for i in range(len(prices)):
            if prices[i]>=prices[sell]:
                sell=i
                profit=prices[sell]-prices[buy] 
                max_profit=max(max_profit,profit)  # max_profit, namely, records the historical maximal profit
            elif prices[i]<=prices[buy]: #Once the buy pointer is updated, we recalculate the profit. 
                buy=i
                sell=i
                profit=0
        return max_profit
