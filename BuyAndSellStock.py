class Solution(object):
    def maxProfit(self, prices):
        
        minPrice = 9223372036854775807
        maxProfit = 0
        
        for price in prices:
            
            if price < minPrice:
                minPrice = price
            
            elif maxProfit < price - minPrice:
                maxProfit = price - minPrice
        return maxProfit
