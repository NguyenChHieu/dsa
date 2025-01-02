class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        pref = [0] * (len(words) + 1)
        for i in range(1, len(words)+1):
            check = 1 if words[i - 1][0] in vowels and words[i - 1][-1] in vowels else 0
            pref[i] += pref[i - 1] + check

        ans = []
        for i in range(len(queries)):
            l, r = queries[i]
            ans.append(pref[r+1] - pref[l])
        return ans
