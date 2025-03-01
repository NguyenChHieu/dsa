class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        ls = []
        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                ls.append(nums[i])
            else:
                count += 1

        for i in range(count):
            ls.append(0)

        return ls
