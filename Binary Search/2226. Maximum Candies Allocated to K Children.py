class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        def check(c_per_ch):
            if c_per_ch == 0:
                return True
            cnt = 0
            for cand in candies:
                cnt += int(cand / c_per_ch)
            return cnt >= k

        l = 0
        r = max(candies)
        result = -1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                result = mid
                l = mid + 1
            else:
                r = mid - 1
        return 0 if result == -1 else result
                
