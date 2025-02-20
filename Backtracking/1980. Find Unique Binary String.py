class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        def backtrack(curr):
            if len(curr) == n:
                st = "".join(curr)
                if st not in nums:
                    return st
                return
            
            for i in range(2):
                curr.append(str(i))
                res = backtrack(curr)
                if res:
                    return res
                curr.pop()
        ans = backtrack([])
        return ans
