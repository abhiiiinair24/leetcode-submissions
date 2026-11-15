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

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n1,n2 = len(str1),len(str2)

        dp = [[-1]*n2 for _ in range(n1)]

        LCS = self.memoisation(n1-1,n2-1,str1,str2,dp)

        ans = []

        i,j = n1-1,n2-1

        while i >= 0 and j >= 0:

            if str1[i] == str2[j]:
                ans.append(str1[i])
                i -=1
                j -=1


            elif self.memoisation(i-1,j,str1,str2,dp) > self.memoisation(i,j-1,str1,str2,dp):
                ans.append(str1[i])
                i -=1
            else:
                ans.append(str2[j])
                j -=1
            
            
        while i >= 0:
            ans.append(str1[i])
            i -=1
        while j >= 0:
            ans.append(str2[j])
            j -=1
        
        #print(ans)

        result = "".join(ans[::-1])

        #print(result)
        return result



                
        