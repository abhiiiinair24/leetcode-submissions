class Solution:
    def memoisation(self,ind,amt,dp,coins):

        if ind == 0:
            if amt % coins[ind] == 0:
                return 1
            else:
                return 0
        
        if dp[ind][amt] != -1:
            return dp[ind][amt]
    

        nottake = self.memoisation(ind-1,amt,dp,coins)
        take = 0
        if amt >= coins[ind]:
            take = self.memoisation(ind,amt-coins[ind],dp,coins)
        
        count = nottake + take

        dp[ind][amt] = count

        return dp[ind][amt]


    def change(self, amount: int, coins: list[int]) -> int:
        
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]

        return self.memoisation(n-1,amount,dp,coins)

        