class Solution:
    def memoisation(self, ind, target,dp,nums):

        if target == 0:
            return True
        
        if ind == 0:
            return nums[ind] == target
        
        if dp[ind][target] != -1:
            return dp[ind][target]
        
        nottake = self.memoisation(ind-1,target,dp,nums)

        take = False
        if target >= nums[ind]:
            take = self.memoisation(ind-1,target-nums[ind],dp,nums)
        

        dp[ind][target] = take or nottake

        return dp[ind][target]
    def canPartition(self, nums: list[int]) -> bool:
        sumv =0
        for i in range(len(nums)):
            sumv += nums[i]
        
        if sumv % 2 != 0:
            return False
    
        target = sumv//2
        n = len(nums)

        dp = [[-1]*(target+1) for _ in range(n)]

        return self.memoisation(n-1,target,dp,nums)



        