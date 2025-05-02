class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # @cache
        # def dp(i, amt):
        #     if amt == 0:
        #         return 1
        #     if i == len(coins) or amt < 0:
        #         return 0
        #     # take or skip
        #     return dp(i, amt - coins[i]) + dp(i+1, amt)
        # return dp(0, amount)

        # precompute every amount that each coin accounts for
        # vd, with coin = 1--> dp = [1,1,1,1,...,1]
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i-coin]
        return dp[amount]
