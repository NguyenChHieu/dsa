class Solution:
    # sliding window
    # think about a relaxed prob - instead of exactly k -> at least k
    # then ans =  num of >=k - num of >= k+1
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.atleastK(word, k) - self.atleastK(word, k+1)
        
    def atleastK(self, word, k):
        l = 0
        v = {'a':0, 'i': 0, 'e': 0, 'u': 0, 'o': 0}
        cos_cnt = 0
        ans = 0

        for r in range(len(word)):
            if word[r] in v:
                v[word[r]] += 1
            else:
                cos_cnt += 1

            while cos_cnt >= k and v['a'] > 0 and v['i'] > 0 and v['e'] > 0 and v['u'] > 0 and v['o'] > 0:
                ans += len(word) - r
                if word[l] in v:
                    v[word[l]] -= 1
                else:
                    cos_cnt -=1 
                l += 1
        return ans
