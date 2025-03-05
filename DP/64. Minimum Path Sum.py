class Solution:
    # 1) func return the min sum of path until (r,c)
    # 2) dp(r,c) = grid[r][c] + min(dp(r-1, c), dp(r, c-1))
    # 3) at the start (0,0) return the starting cell's val


    # iterate each row. Row init as [inf, inf,inf]. Dp[0] init to 0
    # Row-by-Row, Rolling 1D DP Array
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [float('inf')] * (n)
        dp[0] = 0

        for i in range(m):
            new_row = [0] * n
            for j in range(n):
                ans = dp[j]
                if j > 0:
                    ans = min(ans, new_row[j-1])
                new_row[j] = ans + grid[i][j]
            dp = new_row
        return dp[n-1]

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     dp =[[0] * (len(grid[0])+1) for _ in range(len(grid)+1)]
    #     dp[0][0] = grid[0][0]
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if not i and not j:
    #                 continue
    #             ans = float('inf')
    #             if i > 0: # CAN move up
    #                 ans = min(ans, dp[i-1][j])
    #             if j > 0: # can move left
    #                 ans = min(ans, dp[i][j-1])
    #             dp[i][j] = grid[i][j] + ans
    #     return dp[len(grid) -1][len(grid[0]) -1]


    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     @cache
    #     def dp(r, c):
    #         if r == 0 and c == 0:
    #             return grid[r][c]
    #         ans = float('inf')
    #         if r > 0:
    #             ans = min(ans, dp(r-1, c))
    #         if c > 0:
    #             ans = min(ans, dp(r, c-1))
    #         return ans + grid[r][c]
    #     return dp(len(grid) - 1, len(grid[0]) - 1)

    


            
            
