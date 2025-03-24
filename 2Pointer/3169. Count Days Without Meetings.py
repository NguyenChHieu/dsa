class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        r = 0
        ans = 0
        for c_l, c_r in meetings:
            if c_l - r > 1:
                ans += c_l - r - 1
            r = max(r, c_r)
        return ans + days - r
