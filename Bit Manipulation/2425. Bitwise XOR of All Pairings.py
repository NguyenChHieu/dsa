class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        # each element in nums 2 appeared len(nums1) times due 
        # to the cartesian product, so it retains only when
        # it appears odd number of times
        if len(nums1) % 2 == 1:
            for n in nums2:
                ans ^= n

        # similarly.
        if len(nums2) % 2== 1:
            for n in nums1:
                ans ^= n
        return ans
        
