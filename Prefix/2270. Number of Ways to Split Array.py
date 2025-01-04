class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            pref[i] = pref[i - 1] + nums[i - 1]

        ans = 0
        for i in range(1,len(nums)): # the size is n-1 = len(nums) +1 -1
            # fst half sum >= 2nd half sum
            if pref[i] >= pref[-1] - pref[i]:
                ans += 1
        return ans
