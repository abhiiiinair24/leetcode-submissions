class Solution:
    def memoisation(self,i,j,matrix,moves,dp,n,m):

        #Boundary condition
        if i >= n or j >=m:
            return 0
        
        if matrix[i][j] == 0:
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
        
        currentval = 0
        minimum = float('inf')
        for row,col in moves:
            nextrow = i+row
            nextcol = j+col
            currentval = 1 + self.memoisation(nextrow,nextcol,matrix,moves,dp,n,m)
            minimum = min(minimum,currentval)
        
        dp[i][j] = minimum
    
        return dp[i][j]




    def countSquares(self, matrix: list[list[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        dp = [[-1]*m for _ in range(n)]

        moves = [[0,1],[1,1],[1,0]]

        count = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    count += self.memoisation(i,j,matrix,moves,dp,n,m)


        return count

        
        