class Solution:
    def memoisation(self,ind,buy,fee,prices,dp,n):

        if ind == n:
            return 0
        
        if dp[ind][buy] != -1:
            return dp[ind][buy]
        
        if buy:
            profit = max(-prices[ind]+ self.memoisation(ind+1,0,fee,prices,dp,n),0+self.memoisation(ind+1,1,fee,prices,dp,n))
        else:
            profit = max(prices[ind] + self.memoisation(ind+1,1,fee,prices,dp,n)-fee,0+self.memoisation(ind+1,0,fee,prices,dp,n))

        
        dp[ind][buy] = profit

        return dp[ind][buy]

    def maxProfit(self, prices: list[int], fee: int) -> int:

        n = len(prices)

        dp = [[-1]*2 for _ in range(n)]

        return self.memoisation(0,1,fee,prices,dp,n)
        