class Solution:
    def memoisation(self,ind,amt,coins,dp):

        if ind == 0:
            if amt % coins[ind] == 0:
                return amt // coins[ind]
            else:
                return float('inf')

        if dp[ind][amt] != -1:
            return dp[ind][amt]

        nottake = self.memoisation(ind-1,amt,coins,dp)
        take = float('inf')
        if amt >= coins[ind]:
            take = 1 + self.memoisation(ind,amt-coins[ind],coins,dp)
        
        minval = min(take,nottake)

        dp[ind][amt] = minval

        return dp[ind][amt]

    def coinChange(self, coins: list[int], amount: int) -> int:

        n = len(coins)

        # if n == 1:
        #     if amount > coins[0]:
        #         return -1
        
        if amount == 0:
            return 0
        


        dp = [[-1]*(amount+1) for _ in range(n)]

        ans = self.memoisation(n-1,amount,coins,dp)

        if ans == float('inf'):
            return -1
        return ans



        