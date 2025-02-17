class Solution:
    def rob(self, nums: List[int]) -> int:
        #bott-up
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        fst = nums[0]
        sec = max(nums[0], nums[1])
        temp = 0
        for i in range(2, len(nums)):
            temp = max(fst + nums[i], sec)
            fst = sec
            sec = temp
        return temp


        #top down
        # 1
        # def dp(i):
        #     # 3
        #     if i == 0:
        #         return nums[0]
        #     elif i == 1:
        #         return max(nums[0], nums[1])
        #     elif i in save:
        #         return save[i]
            
        #     # 2
        #     save[i] = max(dp(i-2) + nums[i], dp(i-1))
        #     return save[i]
        # save = {}
        # return dp(len(nums)-1)
