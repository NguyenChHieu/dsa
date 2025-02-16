class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        Construct the array dynamically via backtrack(idx)
        using precomputed and boolean arr.

        Base: 
        idx == len(arr) -> found the largest.
        res[idx] != 0 -> skip the alr processed idx.

        Loop from n->1 greedily and process either num = 1 or not.
        Process the num, change arr, mark the boolean arr and backtrack.
        """

        res = [0] * (2 * n -1)
        used = [False] * (n+1)

        def backtrack(idx):
            if idx == len(res):
                return True
            if res[idx] != 0:
                return backtrack(idx+1)

            for i in range(n, 0, -1):
                if used[i]:
                    continue

                if i == 1:
                    used[i] = True
                    res[idx] = 1
                    if backtrack(idx+1):
                        return True
                    used[i] = False
                    res[idx] = 0
                else:
                    if idx + i >= len(res) or res[idx + i] != 0:
                        continue
                    used[i] = True
                    res[idx] = i
                    res[idx + i] = i
                    if backtrack(idx+1):
                        return True
                    used[i] = False
                    res[idx] = 0
                    res[idx + i] = 0
        backtrack(0)
        return res
