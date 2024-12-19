class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # edge
        if grid[0][0] == 1:
            return -1
        def valid(r,c):
            return -1 < r < n and -1 < c < n and grid[r][c] == 0

        n = len(grid)
        queue = deque([(0,0,1)]) # r,c,steps
        seen = {(0,0)}
        d = [(0,1),(0,-1),(1,0),(-1,0),(1,1), (-1,-1), (1,-1),(-1,1)]

        while queue:
            r, c, steps = queue.popleft()
            if (r,c) == (n-1,n-1):# reached the end
                return steps
            
            for dx, dy in d:
                n_r, n_c = r+dx,c+dy
                if valid(n_r,n_c) and (n_r,n_c) not in seen:
                    seen.add((n_r,n_c))
                    queue.append((n_r,n_c,steps+1))
        return -1
