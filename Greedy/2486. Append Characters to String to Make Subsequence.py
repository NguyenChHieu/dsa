class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr = 0
        # 2 pointer
        # simply ptr += 1 if in order, exist a char in s that matches t[ptr]
        for i in range(len(s)):
            if s[i] == t[ptr]:
                ptr += 1
                if ptr == len(t):
                    return 0

        return len(t) - ptr

        
