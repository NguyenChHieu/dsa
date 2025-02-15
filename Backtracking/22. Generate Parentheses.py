class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, r, l):
            if r == 0 and l == 0:
                ans.append(s)
                return 
            # avoid "())(()" and "(" exceed n
            if r < l or l < 0:
                return
            
            backtrack(s + "(", r, l-1)
            backtrack(s + ")", r-1, l)
        
        ans = []
        backtrack("", n, n)
        return ans
