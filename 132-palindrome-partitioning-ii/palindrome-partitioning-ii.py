class Solution:
    def memoisation(self,ind, s, dp,pal):

        if ind == len(s):
            return 0
        
        if dp[ind] != -1:
            return dp[ind]
        

        minimum = float('inf')
        for end in range(ind,len(s)):
            if pal[ind][end]:
                if end == len(s)-1:
                    cuts = 0
                else:
                    cuts = 1 + self.memoisation(end+1,s,dp,pal)
                
                minimum = min(minimum,cuts)

        dp[ind] = minimum

        return dp[ind]

    def minCut(self, s: str) -> int:

        n = len(s)

        dp = [-1]*n

        pal =[[False]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                same_end = s[i] == s[j]
                short = j-i <=2
                if j - i > 2:
                     inner_palindrome = pal[i + 1][j - 1]

                if same_end and (short or inner_palindrome):
                    pal[i][j] = True

        return self.memoisation(0,s,dp,pal)
                
        

 

