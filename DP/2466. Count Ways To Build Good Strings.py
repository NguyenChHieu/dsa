class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Intuition: Backtracking on the length by going down the binary
        decision tree (2 options either add 0/add 1). 
        The branches is guarantee to produce different strings
        since we are adding different options each time we 
        go down the tree and no deletion.
        When reaching the leaf (either its valid/ not valid 
        when checking if the length is in the range).
        Optimize the solution by caching the processed branches.
        """
        # mod = 10 ** 9 + 7
        # dp = {}
        # def dfs(leng):
        #     if leng > high:
        #         return 0
        #     if leng in dp:
        #         return dp[leng]
        #     dp[leng] = 1 if leng >= low else 0
        #     dp[leng] += dfs(leng + zero) + dfs(leng + one)
        #     return dp[leng] % mod
        # return dfs(0) 

        """ dp tabulation 
        keep track of number of ways to form the string
        given a length.

        - Iterate i in [1,high], 
        dp[i - zero]: Represents the number of ways to construct 
        string of length i by appending "zero" to a string of length i - zero.
        dp[i - one]: Represents the number of ways to construct a string 
        of length i by appending "one" to a string of length i - one.
        If i - zero < 0 or i - one < 0, it means that the string length i 
        cannot be reached by appending "zero" or "one" to any smaller 
        valid string, so the dp value for these indices is 0.

        - Sum up the counts in the range.
        """
        dp = {0:1} # 1 way to form an empty string.
        mod = 10 ** 9 + 7

        for i in range(1, high+1):
            dp[i] = (dp.get(i-zero,0) + dp.get(i-one,0)) % mod
        return sum(dp[i] for i in range(low, high+1)) % mod
        
