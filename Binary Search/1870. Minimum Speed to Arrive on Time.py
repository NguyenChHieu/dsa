class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # bs on sol space, with k = speed

        # 1 train need at least (rounded) 1 hr to be reached
        if len(dist) > ceil(hour):
            return -1 

        def check(k):
            t = 0
            for d in dist:
                t = ceil(t)
                t += d/k
            return t <= hour

        l = 1
        r = 10 ** 7

        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
