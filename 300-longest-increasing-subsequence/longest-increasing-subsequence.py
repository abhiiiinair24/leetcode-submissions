class Solution:
    # def memoisation(self,ind,prevind,nums,dp,n):

    #     if ind == n:
    #         return 0


    #     if dp[ind][prevind+1] != -1:
    #         return dp[ind][prevind+1]

    #     nottake = 0 + self.memoisation(ind+1,prevind,nums,dp,n)
    #     take = 0
    #     if prevind == -1 or nums[ind] > nums[prevind]:
    #         take = 1 + self.memoisation(ind+1,ind,nums,dp,n)
        
    #     length = max(take,nottake)

    #     dp[ind][prevind+1] = length

    #     return dp[ind][prevind+1]

    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for ind in range(n):
            for prev in range(ind):
                if nums[prev] < nums[ind]:
                    dp[ind] = max(dp[ind], 1 + dp[prev])

        return max(dp, default=0)

        