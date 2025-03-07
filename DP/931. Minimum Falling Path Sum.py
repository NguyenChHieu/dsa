class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [matrix[0][i] for i in range(n)]

        for i in range(1, n):
            n_dp = [0] * n
            for j in range(n):
                sUm = float('inf')
                if j > 0:
                    sUm = min(sUm, dp[j-1])
                if j < n - 1:
                    sUm = min(sUm, dp[j+1])
                sUm = min(sUm, dp[j])
                n_dp[j] = sUm + matrix[i][j]
            dp = n_dp
        return min(dp)


    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #     n = len(matrix)
    #     dp = [[0] * (n) for _ in range(n)]
    #     for i in range(n):
    #         dp[0][i] = matrix[0][i]
    #     for i in range(1, n):
    #         for j in range(n):
    #             sUm = float('inf')
    #             if j > 0:
    #                 sUm = min(sUm, dp[i-1][j-1])
    #             if j < n - 1:
    #                 sUm = min(sUm, dp[i-1][j+1])
    #             sUm = min(sUm, dp[i-1][j])
    #             dp[i][j] = sUm + matrix[i][j]
    #     return min(dp[n-1][i] for i in range(n))

    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # n = len(matrix)
        # @cache
        # def dp(i, j):
        #     if i == 0:
        #         return matrix[i][j]
        #     sUm = float('inf')
    
        #     if j > 0:
        #         sUm = min(sUm, dp(i-1, j-1))
        #     if j < n - 1:
        #         sUm = min(sUm, dp(i-1, j+1))
        #     sUm = min(sUm, dp(i-1,j))
        #     return matrix[i][j] + sUm
        # ans = float('inf')
        # for i in range(n):
        #     ans = min(ans, dp(n-1, i))
        # return ans
