class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)-1):
            for k in range(i+1,len(words)):
                if len(words[k]) < len(words[i]):
                    continue
                if words[i] in words[k] and \
                    words[k].index(words[i]) == 0 and \
                    words[k].rindex(words[i]) == len(words[k]) - len(words[i]):
                    ans += 1
        return ans
