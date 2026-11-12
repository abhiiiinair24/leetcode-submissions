class Solution:
    def memoisation(self,ind, previndex,nums,dp,n):
        if ind == n:
            return 0
        
        if dp[ind][previndex+1] != -1:
            return dp[ind][previndex+1]
        

        nottake = self.memoisation(ind+1,previndex,nums,dp,n)
        take = 0
        if previndex == -1 or nums[ind] % nums[previndex] == 0 or nums[previndex] % nums[ind] == 0:
            #ans.append(nums[ind])
            take = 1+ self.memoisation(ind+1,ind,nums,dp,n)

        
        dp[ind][previndex+1] = max(nottake,take)

        return dp[ind][previndex+1]


    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        nums = sorted(nums)
        ans = []
        dp = [[-1]*(n+1) for _ in range(n)]

        self.memoisation(0,-1,nums,dp,n)

        ind =0 
        previndex =-1

        while ind < n:

            nottake = self.memoisation(ind + 1, previndex, nums, dp, n)

            if previndex == -1 or nums[ind] % nums[previndex] == 0:
                take = 1 + self.memoisation(ind + 1, ind, nums, dp, n)

                if take >= nottake:
                    ans.append(nums[ind])
                    previndex = ind
                
            ind +=1
        
        return ans




