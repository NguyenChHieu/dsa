class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        seen = set()
        
        def valid(r,c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] != 0
        
        def dfs(r, c, steps):
            steps += grid[r][c]
            seen.add((r,c))
            for dx, dy in dirs:
                nX, nY = r + dx, c + dy
                if valid(nX, nY) and (nX,nY) not in seen:
                    steps = dfs(nX, nY, steps)
            return steps

        ans = 0
        for i in range(R):
            for j in range(C):
                if valid(i,j) and grid[i][j] not in seen:
                    ans = max(ans, dfs(i, j, 0))
        return ans
