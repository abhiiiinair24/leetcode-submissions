class Solution:
    def memoisation(self,ind,k,arr,dp):
        
        if ind == len(arr):
            return 0
        
        if dp[ind][k] != -1:
            return dp[ind][k]
        
        maximumval = float('-inf')

        maximumans = float('-inf')

        length = 0
        for j in range(ind, min(len(arr),ind+k)):
            maximumval = max(maximumval,arr[j])

            length +=1
            print(length)
            summation = maximumval * length + self.memoisation(j+1,k,arr,dp)

            maximumans = max(maximumans,summation)

            dp[ind][k] = maximumans
        
        return dp[ind][k]

    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:

        n = len(arr)
        
        dp = [[-1]*(k+1) for _ in range(n)]

        return self.memoisation(0,k,arr,dp)

        
        