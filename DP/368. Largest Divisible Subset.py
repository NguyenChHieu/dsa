class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n # longest subset upto i
        prev = [-1] * n # keep track of prev i
        maxi = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and \
                    dp[i] < dp[j] + 1: # only update if found a longer sequence
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[maxi]:
                maxi = i
        res = []
        while maxi >= 0:
            res.append(nums[maxi])
            maxi = prev[maxi]
        return res
