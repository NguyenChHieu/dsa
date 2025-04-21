class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # hidden[n+1] - hidden[0] = sum(differences)
        # target = sum(differences)
        # check = set()
        # ans = 0
        # for i in range(lower, upper +1):
        #     if i in check:
        #         ans += 1
        #         continue
        #     check.add(target-i)
        # return ans

        # upper >= max_i >= min_i >=lower 
        #--> upper - max_i = the number needed to create the max prefix
        # similar to lower - min_i
        a = min_i = max_i = 0
        for d in differences:
            a += d
            min_i = min(min_i, a)
            max_i = max(max_i, a)
            if max_i - min_i > upper - lower:
                return 0
        return upper - max_i - (lower-min_i) + 1

