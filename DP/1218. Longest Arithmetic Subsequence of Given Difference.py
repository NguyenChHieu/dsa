class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1

        for num in arr:
            dp[num] = dp.get(num - difference, 0) +1
            ans = max(dp[num], ans)
        return ans
        
        #TLE
        # @cache
        # def dp(i):
        #     ans = 1
        #     for j in range(i):
        #         if arr[i] - arr[j] == difference:
        #             ans = max(ans, 1+dp(j))
        #     return ans
        # return max(dp(i) for i in range((len(arr))))
