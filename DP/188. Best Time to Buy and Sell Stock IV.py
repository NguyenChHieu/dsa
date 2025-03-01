class Solution:
    # dp(i, bought, k) = max(buy,hold,sell)
    # buy = -prices[i] + dp(i+1, True, k)
    # hold = dp(i+1, bought, k)
    # sell = prices[i] + dp(i+1, False, k-1)
    
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (k + 1) for _ in range(2)] for __ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for remain in range(1, k + 1):
                for holding in range(2):
                    ans = dp[i + 1][holding][remain]
                    if holding:
                        ans = max(ans, prices[i] + dp[i + 1][0][remain - 1])
                    else:
                        ans = max(ans, -prices[i] + dp[i + 1][1][remain])
                
                    dp[i][holding][remain] = ans
                
        return dp[0][0][k]
    
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     @cache
    #     def dp(i, bought, remain):
    #         if remain == 0 or i == len(prices):
    #             return 0   
    #         ans = dp(i+1, bought, remain) # hold
    #         if bought:
    #             ans = max(ans, prices[i] + dp(i+1, False, remain - 1)) # sell
    #         else:
    #             ans = max(ans, -prices[i] + dp(i+1, True, remain)) #buy
    #         return ans
    #     return dp(0, False, k)
