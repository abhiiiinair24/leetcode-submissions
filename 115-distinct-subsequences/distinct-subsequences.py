class Solution:
    def memoisation(self,i,j,s,t,dp):
        
        if j < 0:
            return 1 #Indicating i have traversed the entire string and i did get a match and increased the count
        if i < 0:
            return 0

        
        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == t[j]:
            dp[i][j] = self.memoisation(i-1,j-1,s,t,dp) + self.memoisation(i-1,j,s,t,dp)
        else:
            dp[i][j] = self.memoisation(i-1,j,s,t,dp)
        
        return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        
        n1 = len(s)
        n2 = len(t)

        dp = [[-1]*n2 for _ in range(n1)]

        return self.memoisation(n1-1,n2-1,s,t,dp)

