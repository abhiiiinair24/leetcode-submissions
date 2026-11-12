class Solution:
    def isOneCharacterCheck(self,prevword,currword):

        if len(currword) != len(prevword)+1:
            return False
        
        i =0
        for j in range(len(currword)):
            if i < len(prevword) and prevword[i] == currword[j]:
                i +=1
        
        if i == len(prevword):
            return True
        return False

    def memoisation(self,ind,prev,dp,words,n):

        if ind == n:
            return 0
        
        if dp[ind][prev+1] != -1:
            return dp[ind][prev+1]
        

        nottake = self.memoisation(ind+1,prev,dp,words,n)
        take = 0
        if prev == -1 or self.isOneCharacterCheck(words[prev],words[ind]):
            take = 1 + self.memoisation(ind+1,ind,dp,words,n)
        
        dp[ind][prev+1] = max(nottake,take)

        return dp[ind][prev+1]

    def longestStrChain(self, words: list[str]) -> int:

        #words = words.sort(key=len)
        words = sorted(words, key=len)
        print(words)
        n = len(words)
        dp = [[-1]*(n+1) for _ in range(n)]

        return self.memoisation(0,-1,dp,words,n)
        