class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        odd = True if nums[0] % 2 == 1 else False
        for i in range(1, len(nums)):
            if odd and nums[i] % 2 == 1 or (not odd and nums[i] % 2 == 0):
                return False
            odd = True if nums[i] % 2 == 1 else False
        return True

