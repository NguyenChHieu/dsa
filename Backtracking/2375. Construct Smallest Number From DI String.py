class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # backtrack + greedily pick the smallest element
        def backtrack(curr, i, used):
            if i == len(pattern):
                return curr

            if pattern[i] == 'I':
                for j in range(curr[-1], 10): # [last_num, 9]
                    if j in used:
                        continue
                    used.add(j)
                    res = backtrack(curr + [j], i+1, used)
                    if res:
                        return res
                    used.remove(j)
            else:
                for j in range(1, curr[-1]): # [1, last_num]
                    if j in used:
                        continue
                    used.add(j)
                    res = backtrack(curr + [j], i+1, used)
                    if res:
                        return res
                    used.remove(j)
        for i in range(1, 10):
            ans = backtrack([i], 0, {i})
            if ans:
                return "".join(str(x) for x in ans)
        return -1
