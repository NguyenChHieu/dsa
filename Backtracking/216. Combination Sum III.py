class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr, curr_sum, i):
            if len(curr) >= k:
                if len(curr) == k and curr_sum == n:
                    ans.append(curr[:])
                return
            for j in range(i, 10):
                backtrack(curr + [j], curr_sum + j, j+1)
        ans = []
        backtrack([], 0, 1)
        return ans
