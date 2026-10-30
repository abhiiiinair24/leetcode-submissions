class Solution:
    def memoisation(self,i,j1,j2,dp,grid,n,m,moves):

        #Boundary condition
        if j1 < 0 or j1 >=m or j2 < 0 or j2 >=m:
            return float('-inf')
        
        if i == n-1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]
        
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]
            
        maximum = float('-inf')

        for currJ1 in moves:
            for currJ2 in moves:
                nextj1 = j1 + currJ1
                nextj2 = j2 + currJ2

                if j1 == j2:
                    maximum = max(maximum, grid[i][j1]+self.memoisation(i+1,nextj1,nextj2,dp,grid,n,m,moves))
                else:
                    addval = grid[i][j1]+grid[i][j2]
                    maximum = max(maximum, addval+self.memoisation(i+1,nextj1,nextj2,dp,grid,n,m,moves))
        
        dp[i][j1][j2] = maximum

        return dp[i][j1][j2]



    def cherryPickup(self, grid: list[list[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        dp = [[[-1]*m for _ in range(m)] for _ in range(n)]
        moves = [-1,0,1]


        return self.memoisation(0,0,m-1,dp,grid,n,m,moves)



        

        