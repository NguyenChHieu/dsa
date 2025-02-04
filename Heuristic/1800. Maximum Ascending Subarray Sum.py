class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        lim = nums[0]
        curr_sum = nums[0]
        ans = curr_sum

        for i in range(1, len(nums)):
            if nums[i] > lim:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            lim = nums[i]
            ans = max(curr_sum,ans)
        return ans
            
