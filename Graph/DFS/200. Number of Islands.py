class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ensure the visited cell is in the matrix
        def valid(r,c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] == '1'

        def dfs(r, c):
            for dx, dy in d:
                nxt_r, nxt_c = r+dx, c+dy
                if valid(nxt_r,nxt_c):
                    grid[nxt_r][nxt_c] = '0' # mark as visited
                    dfs(nxt_r, nxt_c)
                    
        R = len(grid)
        C = len(grid[0])
        d = [(0,1), (0,-1), (1,0), (-1,0)]
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    ans += 1
                    grid[r][c] == '0'
                    dfs(r,c)
        return ans


