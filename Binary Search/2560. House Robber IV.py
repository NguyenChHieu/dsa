class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def check(guess):
            cnt = 0
            skip = False
            for i in range(len(nums)):
                if not skip and nums[i] <= guess:
                    cnt += 1
                    skip = True
                else:
                    skip = False
                if cnt == k:
                    return True
            return False


        l = min(nums)
        r = max(nums)

        res = float('inf')
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res
