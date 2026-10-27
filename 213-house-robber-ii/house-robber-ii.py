class Solution:
    def recursion(self,ind,dp,nums):
        if ind == 0:
            return nums[0]
        
        if ind < 0:
            return 0
        
        
        if dp[ind] != -1:
            return dp[ind]

        pick = nums[ind] + self.recursion(ind-2,dp,nums)
        nonpick = self.recursion(ind-1,dp,nums)

        dp[ind] = max(pick,nonpick)

        return dp[ind]

    def rob(self, nums: list[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]
        noLastele = [-1]*(n-1)
        for i in range(n-1):
            noLastele[i] = nums[i]
        
        noFirstele = [-1]*(n-1)
        for i in range(1,n):
            noFirstele[i-1] = nums[i]
        
        dp1 =[-1]*(n-1)
        dp2 = [-1]*(n-1)
        ans1 = self.recursion(n-2,dp1,noFirstele)
        ans2 = self.recursion(n-2,dp2,noLastele)
        return max(ans1,ans2)
        # print(noFirstele)
        
        # print(noLastele)
        
        