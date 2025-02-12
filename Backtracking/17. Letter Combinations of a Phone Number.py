class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # i is the pointer to currently-processed digit
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append("".join(curr))
                return
        
            digit = digits[i]
            mapping = comb[digit]
            for idx_ch in range(len(mapping)):
                curr.append(mapping[idx_ch])
                backtrack(curr, i+1)
                curr.pop()
        
        if not digits:
            return []
        
        ans = []
        backtrack([], 0)
        return ans
