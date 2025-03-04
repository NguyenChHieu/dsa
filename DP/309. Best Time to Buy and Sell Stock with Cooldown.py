class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(len(prices) + 1)]
        for i in range(len(prices)-1, -1, -1):
            for bought in range(2):
                for cooldown in range(2):
                    if cooldown:
                        dp[i][bought][cooldown] = dp[i+1][bought][0]
                    else:
                        ans = dp[i+1][bought][cooldown]
                        if bought:
                            ans = max(ans, prices[i] + dp[i+1][0][1])
                        else:
                            ans = max(ans, -prices[i] + dp[i+1][1][cooldown])
                        dp[i][bought][cooldown] = ans
        return dp[0][0][0]

    # def maxProfit(self, prices: List[int]) -> int:
    #     @cache
    #     def dp(i, bought, cooldown):
    #         if i == len(prices):
    #             return 0
    #         if cooldown:
    #             return dp(i+1, bought, False)

    #         ans = dp(i+1, bought, cooldown)
    #         if bought:
    #             ans = max(ans, prices[i] + dp(i+1, False, True))
    #         else:
    #             ans = max(ans, -prices[i] + dp(i+1, True, cooldown))
    #         return ans
    #     return dp(0, False, False)
