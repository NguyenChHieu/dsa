class Solution:
    # loop from start, for each 0 encounter just flip it, if last 2 elements = 1 means that every num is 1
    def minOperations(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        while i <= len(nums) - 3:
            if not nums[i]:
                ans += 1
                nums[i] = 1 if not nums[i] else 0
                nums[i + 1] = 1 if not nums[i + 1] else 0
                nums[i + 2] = 1 if not nums[i + 2] else 0
            i += 1
        return ans if nums[i] and nums[i+1] else -1
