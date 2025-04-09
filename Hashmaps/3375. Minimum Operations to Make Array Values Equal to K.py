class Solution:
    # cant transform any number < k to k.
    # freq of a num > k does not matter,
    # we would know it takes 1 ops to convert it to 
    # k itself or a num > k 
    def minOperations(self, nums: List[int], k: int) -> int:
        c =  set()
        for num in nums:
            if num not in c:
                c.add(num)

        for key in c:
            if key < k:
                return -1
        ans = 0
        for key in c:
            if key > k:
                ans += 1
        return ans
