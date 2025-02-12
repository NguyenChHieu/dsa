class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking, with help of "i" - var that keep track of 
        # where to start iterating through input.

        # since this is subsets, only consider chars that come after i (else it would create dups)

        def backtrack(curr, i):
            # bc
            if i > len(nums):
                return
            
            ans.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j+1)
                curr.pop()
        ans = []
        backtrack([], 0)
        return ans
