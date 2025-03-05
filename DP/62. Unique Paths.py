class Solution:
    # dp(curr pos)
    #dp(r, c) = dp(r-1,c) + dp(r, c-1)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     @cache
    #     def dp(r, c):
    #         if r == 0 and c == 0:
    #             return 1
    #         if not (0<=r<m) or not (0<= c < n):
    #             return 0
            
    #         return dp(r-1, c) + dp(r, c-1) 
    #     return dp(m-1, n-1)
        
