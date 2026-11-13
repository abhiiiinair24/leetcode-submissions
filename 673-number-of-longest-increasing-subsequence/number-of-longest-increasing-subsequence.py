class Solution:
    def memoisation(self,ind,prev,nums,dp,n):

        if ind == n:
            return 0,1
        
        if dp[ind][prev+1] != -1:
            return dp[ind][prev+1]

        nottake_length,nottake_count =self.memoisation(ind+1,prev,nums,dp,n)
        takelength,takecount = 0,0
        if prev == -1 or nums[ind] > nums[prev]:
            takelength,takecount = self.memoisation(ind+1,ind,nums,dp,n)
        
            takelength +=1
        

        if takelength > nottake_length:
            dp[ind][prev+1] = (takelength,takecount)
        elif nottake_length > takelength:
            dp[ind][prev+1] = (nottake_length,nottake_count)
        else:
            dp[ind][prev+1] = (takelength,takecount+nottake_count)
        
        return dp[ind][prev+1]

    def findNumberOfLIS(self, nums: list[int]) -> int:

        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n)]

        length,count = self.memoisation(0,-1,nums,dp,n)

        return count
