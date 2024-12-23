class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(r,c):
            return -1<r<m and -1<c<n and maze[r][c] == '.'
        def escape(r,c):
            if r != entrance[0] \
                or c != entrance[1]:
                return r == 0 or c == 0 or r == m-1 or c == n-1 # border
                
        
        m = len(maze)
        n = len(maze[0])
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = {(entrance[0],entrance[1])}
        q= deque([(entrance[0],entrance[1],0)])

        # only process empty valid cells.
        while q:
            r,c,steps = q.popleft()
            if escape(r,c):
                return steps
            for dx, dy in d:
                nx_r,nx_c = r+dx, c+dy
                if valid(nx_r,nx_c) and (nx_r,nx_c) not in seen:
                    seen.add((nx_r,nx_c))
                    q.append((nx_r,nx_c,steps+1))
        return -1        
