class Solution:
    """
    bott-up
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float("inf")] * (n + 1)
        dp[0] = dp[1] = 0

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]
         
    """
    top down
    """
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     # 1) fn 
    #     def dp(i):
    #         # 3) base cases
    #         if i == 0 or i == 1:
    #             return 0

    #         if i in save:
    #             return save[i]
            
    #         # 2) rec relation
    #         save[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
    #         return save[i]
    #     save = {}
    #     return dp(len(cost))

        
