class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for w in words:
            if pref in w and w.index(pref) == 0:
                ans += 1
        return ans
