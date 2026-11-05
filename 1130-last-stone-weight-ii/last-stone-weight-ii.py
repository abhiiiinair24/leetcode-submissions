class Solution:
    def memoisation(self,ind,target,dp,stones):

        if target == 0:
            return 0
        
        if ind == 0:
            if target >= stones[ind]:
                return stones[ind]
            return 0
        
        if dp[ind][target] != -1:
            return dp[ind][target]
        
        nottake = self.memoisation(ind-1,target,dp,stones)
        take = 0
        if target >= stones[ind]:
            take = stones[ind] + self.memoisation(ind-1,target-stones[ind],dp,stones)
        
        maxval = max(take,nottake)

        dp[ind][target] = maxval

        return dp[ind][target]

    def lastStoneWeightII(self, stones: list[int]) -> int:

        n = len(stones)

        totalsum = sum(stones)

        target = totalsum//2

        dp = [[-1]*(target+1) for _ in range(n)]

        s1 = self.memoisation(n-1,target,dp,stones)
        s2 = totalsum-s1

        return abs(s1-s2)
        
        