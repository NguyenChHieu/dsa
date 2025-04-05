class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, curr, xor):
            if i > len(nums):
                return
            nonlocal ans
            ans += xor
            for j in range(i, len(nums)):
                curr.append(nums[j])
                xor ^= nums[j]
                backtrack(j+1, curr, xor)
                curr.pop()
                xor ^= nums[j]
        ans = 0
        backtrack(0, [], 0)
        return ans
