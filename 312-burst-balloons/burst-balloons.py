class Solution:
    def memoisation(self,i,j,nums,dp):

        if i > j:
            return 0

        
        if dp[i][j] != -1:
            return dp[i][j]
        
        maximum = float('-inf')

        for ind in range(i,j+1):
            coins = nums[i-1] * nums[ind] * nums[j+1] + self.memoisation(i,ind-1,nums,dp) + self.memoisation(ind+1,j,nums,dp)
        
            maximum = max(maximum,coins)
        
        dp[i][j] = maximum

        return dp[i][j]

    def maxCoins(self, nums: list[int]) -> int:

        nums = [1] + nums + [1]
        print(nums)
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]

        return self.memoisation(1,n-2,nums,dp)
         