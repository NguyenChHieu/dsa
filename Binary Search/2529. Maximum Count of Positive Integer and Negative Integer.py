class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = 0  # find (insertion) idx of first 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= 0:
                r = mid
            else:
                l = mid + 1

        l2 = 0  # find (insertion) idx of 1st pos/ next 0
        r2 = len(nums)
        while l2 < r2:
            mid = (l2 + r2) // 2
            if nums[mid] > 0:
                r2 = mid
            else:
                l2 = mid + 1

        neg = l 
        pos = len(nums) - l2
        return max(neg, pos)
        

    # def maximumCount(self, nums: List[int]) -> int:
    #     cnt_pos = 0
    #     cnt_neg = 0
    #     for num in nums:
    #         if num > 0:
    #             cnt_pos += 1
    #         elif num < 0:
