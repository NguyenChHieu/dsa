class Solution:
    # cach bs_right xong bs(upper) - bs(lower-1) hay hon
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bs(l, target, leftmost):
            r = len(nums)
            while l < r:
                mid = (l+r)//2
                if leftmost:
                    if nums[mid] >= target:
                        r = mid
                    else:
                        l = mid + 1
                    continue
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l
        if len(nums) == 1:
            return 1 if lower <= nums[0] <= upper else 0
        nums.sort()
        ans = 0
        for i in range(len(nums)-1):
            left = bs(i+1, lower - nums[i], True)
            right = bs(i+1, upper - nums[i], False)
            ans += right - left
        return ans
