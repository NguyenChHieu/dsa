class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = [(-nums[0], 0)]
        dp = [-float('inf')] * n
        dp[0] = nums[0]
        for i in range(1, n):
            while h and h[0][1] < i - k: # pop out-window eles
                heappop(h)
            dp[i] = nums[i] + (-h[0][0])
            heappush(h, (-dp[i], i))
        return dp[n-1]
