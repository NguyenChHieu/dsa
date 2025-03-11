class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = {'a': 0, 'b': 0, 'c': 0}
        ans = 0
        l = 0

        for r in range(len(s)):
            abc[s[r]] += 1

            # track the idx of curr smallest possible substring that can be formed
            # and every superstring that starts from that idx is valid
            while all(abc.values()):
                ans += len(s) - r
                abc[s[l]] -= 1
                l += 1
        return ans
