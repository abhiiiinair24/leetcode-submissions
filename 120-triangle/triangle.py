class Solution:
    def memoisation(self,ind,col,triangle,dp):
        
        if col < 0 or col >= len(triangle[ind]):
            return float('inf')

        if ind == 0:
            return triangle[0][0]
        
        if dp[ind][col] != -1:
            return dp[ind][col]

        currentupsum = triangle[ind][col] + self.memoisation(ind-1,col,triangle,dp)
        currentdiagonalsum = triangle[ind][col] + self.memoisation(ind-1,col - 1,triangle,dp)

        minimumsum = min(currentupsum,currentdiagonalsum)

        dp[ind][col] = minimumsum
        return dp[ind][col]

    def minimumTotal(self, triangle: list[list[int]]) -> int:

        n = len(triangle)
        m = len(triangle[n-1])

        if n == 1:
            return triangle[0][0]

        #print(triangle[2][2])
        dp = [[-1]*m for i in range(n)]

        # minimum = float('inf')
        # ind = -1
        # for col in range(m):
        #     if minimum > triangle[n-1][col]:
        #         minimum = min(minimum,triangle[n-1][col])
        #         ind = col
        minimum = float('inf')
        for col in range(m):
            minimum = min(minimum,self.memoisation(n-1,col,triangle,dp))
        # print("Minimum value and col: ",minimum,ind)
        return minimum
        
       # print(n,m)
        