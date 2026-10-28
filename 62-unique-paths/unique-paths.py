class Solution:
    def memoisation(self,i,j,dp):
        if i==0 and j ==0:
            return 1
        
        if i < 0 or j < 0:
            return 0
        
        #two possible paths since i m starting from m-1, n-1 i will take opposite direction of down and right ie up and left
        if dp[i][j] != -1:
            return dp[i][j]

        up = self.memoisation(i-1,j,dp)
        left = self.memoisation(i,j-1,dp)

        dp[i][j] = up + left

        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1]*n for i in range(m)]
        print(dp)

        return self.memoisation(m-1,n-1,dp)

        