class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            idx = s.find(part)
            r = idx + len(part)
            s = s[:idx] + s[r:] if r < len(s) else s[:idx]
        return s
