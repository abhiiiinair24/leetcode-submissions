class Solution:
    def memoisation(self,ind,dp,s,wordSet):
        if ind == len(s):
            return True
        
        if dp[ind] != -1:
            return False
        for val in range(ind,len(s)):
            word = s[ind:val+1]

            if word in wordSet:
                if self.memoisation(val+1,dp,s,wordSet):
                    dp[ind] = True
                    return True
            
        dp[ind] = False
        return False
        

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)

        wordSet = set(wordDict)
        print(wordSet)

        dp = [-1]*n

        return self.memoisation(0,dp,s,wordSet)



        