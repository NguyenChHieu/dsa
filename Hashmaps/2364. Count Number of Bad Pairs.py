class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # it equals to nums[i] - i != nums[j] - j
        # count bad pairs = C2n - #good-pairs (sum of C2k, k = cnt[nums[i]-i] that are > 1)

        if len(nums) == 1:
            return 0

        cnt =  {}
        ans = 0
        for i in range(len(nums)):
            cnt[nums[i] - i] = cnt.get(nums[i] - i,0) + 1

        good_pairs = 0
        for v in cnt.values():
            if v > 1:
                good_pairs += factorial(v)//(factorial(v-2) * 2)
        
        return factorial(len(nums))//(factorial(len(nums)-2) * 2) - good_pairs
        
        
        
