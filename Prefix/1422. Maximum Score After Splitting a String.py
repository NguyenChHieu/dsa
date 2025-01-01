class Solution:
    def maxScore(self, s: str) -> int:
        # precompute l = [0,1), r = [1,len(s)]
        l = 1 if s[0] == "0" else 0
        r = 0
        for i in range(1, len(s)):
            if s[i] == "1":
                r += 1
        ans = l + r
        for i in range(1, len(s) - 1):
            if s[i] == "0":
                l += 1
            else:
                r -= 1
            if l+r > ans:
                ans = l+r
        return ans
        
