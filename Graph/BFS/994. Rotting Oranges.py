class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        cnt = 0 # check if possible
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        ans = 0
        while True:
            nxt = deque()
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        nxt.append((nx,ny))
                        grid[nx][ny] = 0
                        cnt -= 1
            q = nxt
            if not q:
                break
            ans += 1
        if cnt != 0:
            return -1
        return ans
            

            

        
