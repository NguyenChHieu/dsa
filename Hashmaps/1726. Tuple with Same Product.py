class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        for i in range(len(nums) - 1):
            for k in range(i + 1,len(nums)):
                product[nums[i] * nums[k]] += 1
            
        ans = 0
        for v in product.values():
            if v > 1:
                # N P 2, a,b (c,d) can switch places so * 2 each
                ans += factorial(v)//factorial(v - 2) * 2 * 2
        return ans
