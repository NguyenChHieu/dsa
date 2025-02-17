class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(curr, freq):
            if len(curr) > len(tiles):
                return

            if curr and curr not in ans:
                ans.add(curr)

            for k in freq.keys():
                if freq[k] == 0:
                    continue
                freq[k] -= 1
                backtrack(curr + k, freq)
                freq[k] += 1

        c = Counter(tiles)
        ans = set()
        backtrack("", c)
        return len(ans)

