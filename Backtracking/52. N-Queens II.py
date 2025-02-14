class Solution:
    def totalNQueens(self, n: int) -> int:
        def valid(x,y,nx,ny):
            return y != ny and abs(nx-x) != abs(ny-y)

        # CURR = loc of all queens placed.
        def backtrack(curr, r):
            nonlocal ans
            if len(curr) == n:
                ans =  ans+1
                return
            
            for c in range(n):
                # new queen pos thoa man every former queen
                if all(valid(x,y,r,c) for x,y in curr):
                    backtrack(curr+[(r,c)],r+1)

        ans = 0
        backtrack([],0)
        return ans
