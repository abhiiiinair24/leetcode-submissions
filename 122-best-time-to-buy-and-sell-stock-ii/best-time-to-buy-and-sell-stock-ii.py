class Solution:
    def memoisation(self,ind,buy,prices,dp,n):

        #Base condition
        if ind == n:
            return 0
        
        if dp[ind][buy] != -1:
            return dp[ind][buy]

        if buy:
            profit = max(-prices[ind] + self.memoisation(ind+1,0,prices,dp,n),0 + self.memoisation(ind+1,1,prices,dp,n))
        else:
            profit = max(prices[ind] + self.memoisation(ind+1,1,prices,dp,n), 0 + self.memoisation(ind+1,0,prices,dp,n))
        

        dp[ind][buy] = profit

        return dp[ind][buy]

    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]

       # print(dp)

        return self.memoisation(0,1,prices,dp,n)


        