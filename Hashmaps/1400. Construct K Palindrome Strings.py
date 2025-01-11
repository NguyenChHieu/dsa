class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        check = 0
        hm = {}
        for c in s:
            hm[c] = hm.get(c,0) + 1

        odd = 0
        for v in hm.values():
            if v % 2 == 1:
                odd += 1

        # minimum number of palindromes would be k, this 
        # is because any 2 odd freq chars can not exist in the
        # same palindrome
        if odd > k:
            return False
        # for any even freq chars, we can always distribute it
        # into a palindrome.
        return True 

