class Solution:
    def memoisation(self,ind, buy,transaction, prices,dp,n):

        if ind == n:
            return 0
        
        if transaction == 0:
            return 0
        
        if dp[ind][buy][transaction] != -1:
            return dp[ind][buy][transaction]

        if buy:
            profit = max(-prices[ind]+ self.memoisation(ind+1,0,transaction,prices,dp,n),0+self.memoisation(ind+1,1,transaction,prices,dp,n))
        
        else:
            profit = max(prices[ind]+ self.memoisation(ind+1,1,transaction-1,prices,dp,n),0+self.memoisation(ind+1,0,transaction,prices,dp,n))

        dp[ind][buy][transaction] = profit

        return dp[ind][buy][transaction]

    def maxProfit(self, prices: list[int]) -> int:
        
        n = len(prices)
        
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n)]

        return self.memoisation(0,1,2,prices,dp,n)

