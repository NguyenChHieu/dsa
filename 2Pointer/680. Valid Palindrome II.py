class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                left = check(s[l:r])
                right = check(s[l+1:r+1])
                return left or right
            else:
                l += 1
                r -= 1
        return True
