class Solution:
    # num_cars = sqrt(time/r)
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 0
        r = max(ranks) * cars * cars

        def check(time):
            n_cars = 0
            for r in ranks:
                n_cars += int(sqrt(time/r)) 
                if n_cars >= cars:
                    return True
            return False
        
        ans = -1
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                r = mid -1
                ans = mid
            else:
                l = mid + 1
        return ans
