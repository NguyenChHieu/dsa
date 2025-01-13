class Solution:
    def minimumLength(self, s: str) -> int:
        """
        As long as a char has freq > 2, there will always
        exist a way to make the freq back to 1 (if odd)
        or 2 (if even). Otherwise if freq <= 2, just keep as is
        """
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        
        ans = 0
        for v in freq.values():
            if v <= 2:
                ans += v
            else:
                if v % 2 == 0:
                    ans += 2
                else:
                    ans += 1
        return ans
