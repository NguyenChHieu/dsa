class Solution:
    # use binary search on 0 -> len(queries) w/ difference array
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(num == 0 for num in nums):
            return 0

        def check_0_array(k):
            pref = [0] * (len(nums) + 1)
            for q in range(k):
                l,r,v = queries[q]
                pref[l] += v
                pref[r + 1] -= v
            num = 0
            for i in range(len(nums)):
                num += pref[i]
                if nums[i] > num:
                    return False
            return True
        
        r = len(queries)
        l = 0
        if not check_0_array(r):
            return -1

        while l <= r:
            mid = (r+l)//2
            if check_0_array(mid):
                r = mid -1
            else:
                l = mid + 1
        return l

    
