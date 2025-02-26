class Solution:
    # compute the "prefix" along the way, and find the greatest and 
    # smallest ele during computing. By using greatest [0,inf] - smallest (could be [-inf, 0])
    # we got the biggest sum
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr = 0 # prefix[0] = 0
        miN = maX = 0
        for i in range(1, len(nums) + 1):
            curr += nums[i-1]
            miN = min(miN, curr)
            maX = max(maX, curr)
        return maX-miN
