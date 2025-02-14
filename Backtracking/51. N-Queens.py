class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(x,y, nx,ny):
            # k can check row vi logic la nx = x +1 --> kbh = nhau
            return ny != y and abs(nx-x) != abs(ny-y)

        def backtrack(curr, row):
            # if all queens were placed
            if len(curr) == n:
                board = [["." for _ in range(n)] for _ in range(n)]
                for x, y in curr:
                    board[x][y] = "Q"
                ans.append(["".join(x) for x in board])
                return 
            
            for col in range(n):
                if all(valid(x,y, row,col) for x,y in curr):
                    backtrack(curr + [(row, col)], row+1)
        ans = []
        backtrack([], 0)
        return ans

