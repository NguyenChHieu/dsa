class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # just iterate over the unique chars, if a letter only occur once,
        # the below inner loop wont run.
        letters = set(s)  
        ans = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            # check for all unique char between 2 similar chars
            for k in range(i+1,j):
                between.add(s[k])
            
            ans += len(between)
        return ans
