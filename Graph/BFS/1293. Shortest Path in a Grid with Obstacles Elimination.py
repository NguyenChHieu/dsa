class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # simply perform bfs on the grid but seen will store(coords, k)

        def valid(r,c):
            return -1<r<m and -1<c<n 

        m = len(grid)
        n = len(grid[0])
        d= [(0,1),(0,-1),(1,0), (-1,0)]
        seen = {(0,0,k)}
        q = deque([(0,0,0,k)])

        while q:
            r,c,steps,remain = q.popleft()
            if r == m-1 and c == n-1:
                return steps
            for dx, dy in d:
                nx_r, nx_c = r+dx, c+dy
                if valid(nx_r, nx_c):
                    if grid[nx_r][nx_c] == 1: # obstacle
                        if remain >0 and (nx_r,nx_c,remain-1) not in seen:
                            seen.add((nx_r, nx_c,remain-1))
                            q.append((nx_r, nx_c, steps+1, remain-1))
                    else:
                        if (nx_r,nx_c,remain) not in seen:
                            seen.add((nx_r, nx_c,remain))
                            q.append((nx_r, nx_c, steps+1, remain))
        return -1




