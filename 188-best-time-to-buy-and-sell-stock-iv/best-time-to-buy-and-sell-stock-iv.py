class Solution:
    def memoisation(self,ind, buy,k, prices,dp,n):
        if ind == n:
            return 0
        
        if k == 0:
            return 0
        
        if dp[ind][buy][k] != -1:
            return dp[ind][buy][k]

        if buy:
            profit = max(-prices[ind]+ self.memoisation(ind+1,0,k,prices,dp,n),0+self.memoisation(ind+1,1,k,prices,dp,n))
        
        else:
            profit = max(prices[ind]+ self.memoisation(ind+1,1,k-1,prices,dp,n),0+self.memoisation(ind+1,0,k,prices,dp,n))

        dp[ind][buy][k] = profit

        return dp[ind][buy][k]

    def maxProfit(self, k: int, prices: list[int]) -> int:

        n = len(prices)

        dp = [[[-1]*(k+1) for _ in range(2)] for _ in range(n)]

        return self.memoisation(0,1,k,prices,dp,n)        
        