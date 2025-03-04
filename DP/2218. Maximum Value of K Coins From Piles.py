class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [[0] * (k+1) for _ in range(len(piles)+1)]
        for i in range(len(piles) -1, -1, -1):
            for remain in range(1, k+1):
                dp[i][remain] = dp[i+1][remain]
                curr = 0
                for j in range(min(len(piles[i]), remain)):
                    curr += piles[i][j]
                    dp[i][remain] = max(dp[i][remain], curr + dp[i+1][remain - j - 1])
        return dp[0][k]

    # def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
    #     @cache
    #     def dp(i, k_remain):
    #         if k_remain == 0 or i == len(piles):
    #             return 0

    #         # dp(i, remain) = max(take, skip)
    #         # skip = dp(i+1, remain)
    #         # take = max(total took from current pile + dp(i+1, remaining takes)
    #         # from 0,min(remain, pile length)
    #         ans = dp(i+1, k_remain)
    #         curr = 0
    #         for j in range(min(k_remain, len(piles[i]))):
    #             curr += piles[i][j]
    #             ans = max(ans, curr + dp(i+1, k_remain - j -1))
    #         return ans
    #     return dp(0, k)


