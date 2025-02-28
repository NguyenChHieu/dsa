class Solution:
    # dp(i,j) return the LCS start at i and end at j of text2
    # at each pair i,j:
    # text1[i] = text2[j] -> dp(i,j) = 1 + dp(i+1, j+1)
    # either move up a char in text1 or text2
    # text1[i] = text2[j] -> dp(i, j) = max(dp(i + 1, j), dp(i, j + 1))
    
    # base: i = text1.length/ k = text2.length

    # bott-up
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

    # topdown
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     @cache
    #     def dp(i, j):
    #         if i == len(text1) or j == len(text2):
    #             return 0
    #         if text1[i] == text2[j]:
    #             return 1 + dp(i+1,j+1) 
    #         return max(dp(i+1,j), dp(i,j+1))
    #     return dp(0,0)
