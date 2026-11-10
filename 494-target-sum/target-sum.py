class Solution:
    def memoisation(self,ind,target,nums,dp):

        if ind < 0:
            if target == 0:
                return 1
            return 0
        
        if dp[ind][target] != -1:
            return dp[ind][target]
        

        nottake = self.memoisation(ind-1,target,nums,dp)
        take = 0
        if target >= nums[ind]:
            take = self.memoisation(ind-1,target-nums[ind],nums,dp)
        
        count = take + nottake

        dp[ind][target] = count

        return dp[ind][target]

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        
        n = len(nums)

        totalsum = sum(nums)

        if (totalsum - target) >= 0 and (totalsum-target) %2 == 0:
            target = (totalsum - target) // 2
            #print(target)
        else:
            return 0

        dp = [[-1]*(target+1) for _ in range(n)]

        return self.memoisation(n-1,target,nums,dp)