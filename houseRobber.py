# Recursion + Memoized solution

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.dp = [-1 for i in range(len(nums))]
        return self.robDp(0)
        
    def robDp(self,n):
        if n < len(self.nums)-1:
            if self.dp[n] != -1: 
                return self.dp[n]
            self.dp[n] = max(self.nums[n] + self.robDp(n+2), self.robDp(n+1))
            return self.dp[n]
        elif n == len(self.nums)-1:
            return self.nums[n]
        else:
            return 0



# Iterative Solution

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==0):
            return 0
        
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1,n):
            if(i==1):
                dp[i] = max(nums[0],nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return dp[-1]