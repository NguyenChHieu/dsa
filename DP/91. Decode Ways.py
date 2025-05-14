class Solution:
    # dp(st) - how many ways to construct string st
    # bc - empty st - 1 way; st starts with 0 -> 0 way; length-1 st - 1 way
    # r.step - st[0] in mapping - check for potential ways, st[:2] - check for potential ways

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        if not n or s[0] == '0':
            return 0
        dp[1] = 1
        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]
        return dp[n]

    # def numDecodings(self, s: str) -> int:
    #     @cache
    #     def dp(st):
    #         if not st:
    #             return 1
    #         if st[0] == '0':
    #             return 0
    #         if len(st) == 1:
    #             return 1
    #         fst = st[0]
    #         sec = st[:2]
    #         total = 0
    #         if fst != '0':
    #             total += dp(st[1:])
    #         if 10 <= int(sec) < 27:
    #             total += dp(st[2:])
    #         return total
    #     return dp(s)
