class Solution:
    """
    3 states: 
    fully filled (dp[i][0]), 
    dangling top cell dp[i][1], 
    dangling bot cell dp[i][2]
    0)
    -> add 1 vert line from dp[i-1][0], add 2 hor line from dp[i-2][0]
    -> add 1 tromino from dp[i-2][1] or dp[i-2][2]
    1)
    - dp[i-1][0] add a tromino
    - dp[i-1][2] match the bot tromino
    2)
    - dp[i-1][0] add a tromino
    - dp[i-1][1] match the top tromino
    """
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * 3 for i in range(n+1)]
        # k co gi; placed a vert domino
        dp[0][0] = dp[1][0] = 1
        # tromino filled bot; tromino filled top
        dp[1][1] = dp[1][2] = 1

        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-2][1] + dp[i-2][2]) % mod
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % mod
        return int(dp[n][0])
