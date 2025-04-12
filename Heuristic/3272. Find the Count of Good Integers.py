class Solution:
    """
    Generate palindromes (e.g., 121, 505).
    For each:
    Check divisibility by k.
    Compute permutations minus invalid ones.
    Track unique palindromes via frequency.
    Sum valid counts.
    """
    def countGoodIntegers(self, n: int, k: int) -> int:
        # list of digits to int
        def build_num(vector):
            res = 0
            for num in vector:
                res = res * 10 + num
            return res
        # calc # of distinct perms
        # total digit count! / dups!
        def perm(freqMap, total):
            res = factorial(total)
            for cnt in freqMap.values():
                res //= factorial(cnt)
            return res
        # calc perms that start with 0
        def perm0(freqMap, total):
            if freqMap.get(0,0) == 0:
                return 0
            freqMap[0] -= 1
            res = factorial(total - 1)
            for cnt in freqMap.values():
                res //= factorial(cnt)
            return res
        """
        Recursively builds palindromes:
        Fills digits symmetrically (left, right).
        Base case: Checks divisibility by k, adds valid permutations if unique.
        Ensures first digit is non-zero.
        """
        def genPal(pal, l, r, div, total):
            nonlocal ans
            if l > r:
                pal_num = build_num(pal)
                if pal_num % div == 0:
                    freq = Counter(pal)
                    key = tuple(sorted(freq.items()))
                    if key not in seen:
                        ans += perm(freq, total) - perm0(freq, total)
                        seen.add(key)
                return 
            for d in range(1 if l == 0 else 0,10):
                pal[l] = pal[r] = d
                genPal(pal, l+1, r-1, div, total)
        ans = 0
        seen = set()
        genPal([0] * n, 0, n-1, k, n)
        return ans
