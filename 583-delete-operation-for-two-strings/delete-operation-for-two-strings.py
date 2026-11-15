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

    def minDistance(self, word1: str, word2: str) -> int:

        n1 = len(word1)
        n2 = len(word2)

        
        # print(n1,n2)

        dp = [[-1]*(n2+1) for _ in range(n1)]

        LCS = self.memoisation(n1-1,n2-1,word1,word2,dp)

        if LCS != min(n1,n2):
            return n1+n2 -(2*LCS)
        else:
            return max(n1,n2)-LCS
        