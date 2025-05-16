class Solution:
    # LIS + tracking longest seq
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming(s1, s2):
            if len(s1) != len(s2):
                return False
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                if diff > 1:
                    break
            return diff == 1

        @cache
        def dp(i):
            best = 1
            for j in range(i):
                if groups[j] != groups[i] and hamming(words[j], words[i]):
                    new = dp(j) + 1
                    if new > best: # if a later seq satisfy the above cond, it might override the answer (if smaller)
                        best  = dp(j) + 1
                        prev[i] = j
            return best 

        prev = [-1] * len(words)
        max_idx = - 1
        curr = 0
        for k in range(len(words)):
            val = dp(k)
            if val > curr:
                max_idx = k
                curr = val
        ans = []
        while max_idx != -1:
            ans.append(words[max_idx])
            max_idx = prev[max_idx]
        return ans[::-1]
