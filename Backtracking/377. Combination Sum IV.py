class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def backtrack(curr):
            if curr > target:
                return 0
            if curr == target:
                return 1
            total = 0
            for i in range(len(nums)):
                total += backtrack(curr + nums[i])
            return total
        return backtrack(0)

