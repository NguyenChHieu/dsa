class Solution:
    """
    Find LCS (#1143)
    Backtrack to find LCS
    Build SCS around the LCS using pointers, prioritize 
    non-matching characters!
    """
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # backtrack to find lcs
        # start at dp[0,0], if str1[i] == str2[j]
        # that means we found a matching char, move diag
        # else go to the direction which has a higher value --> longer lcs
        i, j = 0, 0
        lcs = []
        while i < n and j < m:
            if str1[i] == str2[j]:
                lcs.append(str1[i])
                i += 1
                j += 1
            elif dp[i+1][j] > dp[i][j+1]:
                i += 1
            else:
                j += 1
        lcs = "".join(lcs)
        ans = []
        fst, sec = 0, 0
        for c in lcs:
            while str1[fst] != c:
                ans.append(str1[fst])
                fst += 1
            while str2[sec] != c:
                ans.append(str2[sec])
                sec += 1
            ans.append(c)
            fst += 1
            sec += 1
        ans.extend(str1[fst:])
        ans.extend(str2[sec:])
        return "".join(ans)
