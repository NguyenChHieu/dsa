class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(k):
            sums = 0
            for num in nums:
                sums  += ceil(num / k)
            return sums <= threshold
        
        l = 1
        r = 10 ** 6

        while l <= r:
            mid = (l+r) //2
            if check(mid):
                r = mid-1
            else:
                l = mid + 1
        return l
