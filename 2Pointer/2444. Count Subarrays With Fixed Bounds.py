class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        st, m, M = -1,-1,-1 # last invalid idx/ last idx of minK/ last idx of maxK
        ans = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                st = i
            # not elif bcs minK can = maxK
            if nums[i] == minK:
                m = i
            if nums[i] == maxK:
                M = i
            # only care about:
            # 1: both m, M is > st? yes -> a valid subarr must exist, 
            # else if either m/M <= st or both, it would makes the subtraction <= 0 --> max(0,...) = 0
            ans += max(0, min(m, M) - st) 
        return ans
