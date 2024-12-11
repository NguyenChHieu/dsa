class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # sort array and treat it as a sliding window problem.
        nums.sort()
        final  = 0
        ans = 0
        l = 0
        for i in range(len(nums)):
            ans += 1
            while nums[i] - nums[l] > 2 * k: # the subtraction = 2k.
                ans -= 1
                l += 1
            final = max(final, ans)
        return final