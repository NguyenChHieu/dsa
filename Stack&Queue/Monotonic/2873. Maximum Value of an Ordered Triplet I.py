class Solution:
    # monotonic desc + suffix arr
    def maximumTripletValue(self, nums: List[int]) -> int:
        suffix = nums.copy()
        curr = nums[len(nums)-1]
        for i in range(len(nums) - 1, -1 ,-1):
            if suffix[i] < curr:
                suffix[i] = curr
            elif suffix[i] > curr:
                curr = suffix[i]
        ans = 0
        fst =  nums[0]
        for i in range(1, len(nums) - 1):
            if fst < nums[i]:
                fst = nums[i]
                continue
            ans = max((fst - nums[i]) * suffix[i+1], ans)
        return ans
        
