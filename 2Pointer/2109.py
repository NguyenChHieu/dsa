class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        p1 = 0
        p2 = 0

        ans = ""

        i = 0
        while p1 < len(s) and p2 < len(spaces):
            if i == spaces[p2]:
                ans += " "
                p2 += 1
            else:
                ans += s[p1]
                p1 += 1
                i += 1

        while p1 < len(s):
            ans += s[p1]
            p1 += 1

        while p1 < len(s):
            ans += " "
            p2 += 1

        return ans