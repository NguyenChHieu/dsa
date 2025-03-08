class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = 0
        count = 0
        while r - l < k:
            count += 1 if blocks[r] == 'W' else 0
            r += 1
        ans = count
        for i in range(r, len(blocks)):
            count += 1 if blocks[i] == 'W' else 0
            count -= 1 if blocks[l] == 'W' else 0
            l += 1
            ans = min(ans, count)
        return ans
