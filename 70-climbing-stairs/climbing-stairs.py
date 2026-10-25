class Solution:
    def memoisation(self,n,dp):
        if n < 0:
            return 0
        if n == 0:
            return 1
        
        if dp[n] != -1:
            return dp[n]


        left = self.memoisation(n-1,dp)
        right = self.memoisation(n-2,dp)

        dp[n] = left + right

        return dp[n]
    def climbStairs(self, n: int) -> int:
        
        dp = [-1]*(n+1)

        return self.memoisation(n,dp)

         