class Solution:
    def memoisation(self,i,j,s,p,dp):
        if i < 0 and j < 0:
             return True    

        if j < 0:
            return False
        
        if i < 0:
            return all(char == "*" for char in p[:j+1]) #returns True if all condition matches 
            #one fails that itself returns False

        if dp[i][j] is not None:
            return dp[i][j]

        if s[i] == p[j] or p[j] == '?':
            dp[i][j] = self.memoisation(i-1,j-1,s,p,dp)
        
        elif p[j] == '*':
            dp [i][j] = (self.memoisation(i-1,j,s,p,dp) or self.memoisation(i,j-1,s,p,dp))
        else:
            dp[i][j] = False

        return dp[i][j]



    def isMatch(self, s: str, p: str) -> bool:

        n1 = len(s)
        n2 = len(p)

        dp = [[None]*n2 for _ in range(n1)]

        return self.memoisation(n1-1,n2-1,s,p,dp)
        