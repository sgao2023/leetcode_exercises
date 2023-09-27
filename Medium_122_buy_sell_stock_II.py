class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0
        sell=0
        profit=0
        total_profit=0
        flag=-1
        if len(prices)==1: return 0

        for i in range(1,len(prices)):
            if prices[i]>=prices[i-1]:
                sell=i
                profit=prices[sell]-prices[buy]
                flag=-1
            elif prices[i]<=prices[i-1]:
                buy=i
                sell=i
                total_profit+=profit
                profit=0
                flag=1
#check if there's remaining unsold stock
        if flag==-1:
            total_profit+=profit
        return total_profit
