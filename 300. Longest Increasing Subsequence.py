class Solution:
    # bottup
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            lis = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    lis = max(lis, dp[j] + 1)
            dp[i] = lis
        return max(dp)


    # top down
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     memo = {}

    #     def dp(i):
    #         if i in memo:
    #             return memo[i]
    #         # 3
    #         ans = 1

    #         # 2
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 ans = max(ans, dp(j) + 1)
    #         memo[i] = ans
    #         return ans
    #     return max(dp(k) for k in range(len(nums)))
