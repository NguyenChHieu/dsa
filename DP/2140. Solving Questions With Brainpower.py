class Solution:
    # bot-up
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[min(n,i+1)], questions[i][0] + dp[min(i+questions[i][1] + 1, n)])
        return dp[0]
    # top down
    # def mostPoints(self, questions: List[List[int]]) -> int:
    #     @cache
    #     def dp(i):
    #         if i >= len(questions):
    #             return 0
    #         # either skip the question or do it and skip the next (i + q[i][1]) questions
    #         return max(dp(i + 1), questions[i][0] + dp(i + questions[i][1] + 1))
    #     return dp(0)
