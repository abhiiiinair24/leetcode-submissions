class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        smallestPrice = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            diff = prices[i] - smallestPrice
            maxprofit = max(maxprofit,diff)
            smallestPrice = min(smallestPrice,prices[i])
        
        return maxprofit





        