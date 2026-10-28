class Solution:
    def memoisation(self,i,j,dp,obstacleGrid):

        if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
            return 1
        
        if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
            return 0
        

        if dp[i][j] != -1:
            return dp[i][j]

        up = self.memoisation(i-1,j,dp,obstacleGrid)
        left = self.memoisation(i,j-1,dp,obstacleGrid)

        dp[i][j] = up + left

        return dp[i][j]
        
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:


        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m==1 and n==1 and obstacleGrid[0][0] != 1:
            return 1


        dp = [[-1]*n for i in range(m)]

        
        return self.memoisation(m-1,n-1,dp,obstacleGrid)
        