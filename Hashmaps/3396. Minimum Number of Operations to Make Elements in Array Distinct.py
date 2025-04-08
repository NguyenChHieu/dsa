class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = math.ceil(len(nums) / 3)
        remain = len(nums) % 3

        c = Counter(nums)
        dups = {k: v for k, v in c.items() if v > 1}
        if not dups:
            return 0

        ans = 0
        for group in range(n):
            start = group * 3
            size = 3 if group != n - 1 else (3 if remain == 0 else remain)
            for j in range(size):
                val = nums[start + j]
                if val in dups:
                    dups[val] -= 1
                    if dups[val] < 2:
                        del dups[val]
            ans += 1
            if not dups:
                return ans
        return ans

                
                
        
