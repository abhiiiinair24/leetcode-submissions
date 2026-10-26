class Solution:
    def recursion(self,ind,dp,nums):

        if ind == 0:
            return nums[0]
        
        if ind < 0:
            return 0
        
        if dp[ind] != -1:
            return dp[ind]
        
        pick = nums[ind] + self.recursion(ind-2,dp,nums)
        notrob = self.recursion(ind-1,dp,nums)

        dp[ind] = max(pick,notrob)

        return dp[ind]
    def rob(self, nums: list[int]) -> int:

        n = len(nums)

        dp = [-1]*n

        return self.recursion(n-1,dp,nums)



        