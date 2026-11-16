class Solution:
    def memoisation(self,i,j,word1,word2,dp):

        if j < 0:
            return i+1
        
        if i < 0:
            return j+1

        if dp[i][j] != -1:
            return dp[i][j]

        if word1[i] == word2[j]:
            dp[i][j] = 0 + self.memoisation(i-1,j-1,word1,word2,dp)
        
        else:
            dp[i][j] = min(1+self.memoisation(i-1,j,word1,word2,dp),1+self.memoisation(i,j-1,word1,word2,dp),1+self.memoisation(i-1,j-1,word1,word2,dp))

        return dp[i][j]
    def minDistance(self, word1: str, word2: str) -> int:

        n1 = len(word1)
        n2 = len(word2)

        dp = [[-1]*n2 for _ in range(n1)]

        return self.memoisation(n1-1,n2-1,word1,word2,dp)

        