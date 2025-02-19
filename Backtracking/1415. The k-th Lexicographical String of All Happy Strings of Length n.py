class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(curr):
            if len(curr) == n:
                curr = "".join(curr)
                ans.append(curr)
                return

            for l in letters:
                if not curr:
                    backtrack(curr + [l])
                else:
                    if curr[-1] != l:
                        curr.append(l)
                        backtrack(curr)
                        curr.pop()

        ans = []
        letters = ['a', 'b', 'c']
        backtrack([])
        return "" if k > len(ans) else ans[k - 1]
