class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtrack with "i" - in order to avoid dups (e.g, target 5, cand=[2,3])
        # if no "i" then it would produce [2,3] and [3,2]  
        
        # "i" here can be the same last char, since it can be used an unlimited number of times.

        # TC O(n^(T/M)) - T = height tree, M = smallest number --> repeatedly use M til it exceeds target

        def backtrack(curr, curr_sum, i):
            if curr_sum == target:
                ans.append(curr)
                return
            
            if curr_sum > target:
                return
            
            for j in range(i, len(candidates)):
                num = candidates[j]
                backtrack(curr + [num], curr_sum+num, j)
        ans = []
        backtrack([], 0, 0)
        return ans
