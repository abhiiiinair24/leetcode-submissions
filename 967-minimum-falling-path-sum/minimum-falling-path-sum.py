class Solution:
    def memoisastion(self,ind,col,matrix,moves,dp,n):
        if col >=n or col < 0:
            return float('inf')

        if ind == 0 and col < n and col >= 0:
            return matrix[0][col]
        
        if dp[ind][col] != None:
            return dp[ind][col]
        
        minimumval = float('inf')
        for row,currcol in moves:
             cost= matrix[ind][col] + self.memoisastion(ind-row,col+currcol,matrix,moves,dp,n)
             minimumval = min(minimumval,cost)
    
        dp[ind][col] = minimumval

        return dp[ind][col]

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        dp = [[None]*n for i in range(m)]

        moves = [[1,-1],[1,0],[1,1]]

        minimum = float('inf')

        for col in range(n):
            minimum = min(minimum,self.memoisastion(m-1,col,matrix,moves,dp,n))
            
        return minimum