class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # bs on sol spaces, with min ans possible = 1 and max possible max(piles)
        def check(k):
            hrs = 0
            for p in piles:
                hrs += ceil(p/k)
            return hrs <= h

        l = 1
        r = max(piles)

        while l <= r:
            mid = (l+r) // 2
            # can still improve
            if check(mid):
                r = mid -1
            else:
                l = mid +1
        return l
