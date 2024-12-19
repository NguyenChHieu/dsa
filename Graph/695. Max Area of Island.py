class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = set()
        
        def valid(r,c):
            return -1 < r < R and -1 < c < C and grid[r][c] == 1
        
        def dfs(r,c):
            cnt = 1
            for dx, dy in d:
                n_r,n_c = r+dx, c+dy
                if valid(n_r,n_c) and (n_r, n_c) not in seen:
                    seen.add((n_r, n_c))
                    cnt += dfs(n_r, n_c)
            return cnt

        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in seen:
                    seen.add((r,c))
                    area = dfs(r,c)
                    ans = max(area,ans)
        return ans
