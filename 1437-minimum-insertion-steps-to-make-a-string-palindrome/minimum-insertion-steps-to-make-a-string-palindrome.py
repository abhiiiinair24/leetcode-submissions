class Solution:
    def memoisation(self,ind1,ind2,text1,text2,dp):

        if ind1 < 0 or ind2 < 0:
            return 0
        
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]
        
        match,notmatch = 0,0
        if text1[ind1] == text2[ind2]:
            match = 1 + self.memoisation(ind1-1,ind2-1,text1,text2,dp)
        else:
            notmatch = 0 + max(self.memoisation(ind1-1,ind2,text1,text2,dp),self.memoisation(ind1,ind2-1,text1,text2,dp))
        

        result = match+notmatch
        dp[ind1][ind2] = result

        return dp[ind1][ind2]

    def minInsertions(self, s: str) -> int:

        n = len(s)

        s2 = s[::-1]

        dp = [[-1]*n for _ in range(n)]

        insertionSteps =  self.memoisation(n-1,n-1,s,s2,dp)

        return (n-insertionSteps)

        