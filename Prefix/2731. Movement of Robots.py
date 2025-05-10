class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for i in range(len(nums)):
            nums[i] += (-d if s[i] == 'L' else d)
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            add = (len(nums) - 1 - i) * -nums[i] + i * nums[i]
            ans += add % (10**9 + 7)
        return ans % (10**9 + 7)
