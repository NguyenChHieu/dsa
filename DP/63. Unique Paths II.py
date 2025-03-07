class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] *(n+1) for _ in range(m+1)]
        if obstacleGrid[0][0]:
            return 0 
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i + j == 0:
                    continue
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                    continue
                ans = 0
                if i > 0:
                    ans += dp[i-1][j]
                if j > 0:
                    ans += dp[i][j-1]
                dp[i][j] = ans
        return dp[m-1][n-1]


    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # @cache
        # def dp(i,j):
        #     if i + j == 0:
        #         return 1
        #     if obstacleGrid[i][j]:
        #         return 0
        #     ans = 0
        #     if i > 0:
        #         ans += dp(i-1,j)
        #     if j > 0:
        #         ans += dp(i, j-1)
        #     return ans 
        # # entrance block
        # if obstacleGrid[0][0]:
        #     return 0 
        # return dp(len(obstacleGrid) - 1, len(obstacleGrid[0]) -1)
