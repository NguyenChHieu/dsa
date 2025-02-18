class Solution:
    # bottom up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        ans = dp[amount]
        return ans if ans != float('inf') else -1
        
    # top down
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     memo = defaultdict(lambda: float('inf'))
    #     def dp(i):
    #         if i == 0:
    #             return 0
    #         if i in memo:
    #             return memo[i]

    #         for c in coins:
    #             if c <= i:
    #                 # Compare either 
    #                 # 1) sum = i hasnt yet had a combination/ exist at least 1 combination that makes up i
    #                 # 2) find another way to construct the sum (taking one of the coins into account) with
    #                 #    the min coins that construct sum = i-c
    #                 memo[i] = min(memo[i], dp(i-c) + 1)
    #         return memo[i]
    #     ans = dp(amount)
    #     return ans if ans != float('inf') else -1

