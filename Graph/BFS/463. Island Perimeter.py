class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        
        start = None
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i,j)
                    ans += 4
                    break
            if start:
                break
        
        q = deque([start])
        seen = {start}
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx,ny = x+dx, y+dy
                if 0<=nx<m and 0<= ny<n and grid[nx][ny] and (nx,ny) not in seen:
                    ans += 4
                    if (nx-1,ny) in seen:  
                        ans -= 2
                    if (nx+1,ny) in seen:
                        ans -= 2
                    if (nx,ny-1) in seen:
                        ans -= 2
                    if (nx,ny+1) in seen:
                        ans -= 2
                    seen.add((nx,ny))
                    q.append((nx,ny))
        return ans

        # normal traversal also work
