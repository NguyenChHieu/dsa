class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        ans = 1
        fst = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if fst == -1:
                    fst = i
                    continue
                ans *= (i-fst)
                fst = i
        return ans % (10**9 + 7) if fst != -1 else 0 
