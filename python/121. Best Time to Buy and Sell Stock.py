class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left, right = 0,1 # left = buy and right = sell pointer
        
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        while right < len(prices):
            #checks profitability 
            if prices[left]<prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        
#sliding window
#time 0(n)
#space 0(1)
        