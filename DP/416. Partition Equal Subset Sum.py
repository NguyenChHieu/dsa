class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        n = len(nums)
        dp = [False] * (target + 1) # dp[i] = whether sum i is reachable
        dp[0] = True
        for num in nums:
            # prevents the same number from being counted multiple times
            for i in range(target, num - 1, -1): 
                dp[i] = dp[i] or dp[i-num]
        return dp[target]

        # backtracking w memo
        # nums.sort()
        # @cache
        # def backtrack(i, curr):
        #     if curr > target or i > n:
        #         return False
        #     if curr == target:
        #         return True
        #     for j in range(i, n):
        #         check = backtrack(j+1, curr + nums[j])
        #         if check:
        #             return True
        #     return False
        # return backtrack(0, 0)
