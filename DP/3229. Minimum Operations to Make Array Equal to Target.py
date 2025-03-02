class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        diff = [nums[i] - target[i] for i in range(len(nums))]
        ans = diff[0] if diff[0] > 0 else -diff[0]
        prev = diff[0]

        for i in range(1,len(nums)):
            if diff[i] == 0:
                prev = 0
                continue
            if prev < 0:
                ans += diff[i] if diff[i] > 0 else max(0, prev - diff[i])
            else:
                ans += -diff[i] if diff[i] < 0 else max(0, diff[i] - prev)
            prev = diff[i]
        return ans
