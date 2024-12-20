class Solution:
    # k có dups vì các ô sẽ được marked bởi ô số 0 gần nhất, và đồng thời
    # nó cũng được marked trong seen nên sẽ k bị overwritten
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(r,c):
            return -1 < r < len(mat) and -1 < c < len(mat[0]) and mat[r][c] == 1
        
        m = len(mat)
        n = len(mat[0])
        seen = set()
        queue = deque()
        d = [(0,1), (0,-1), (1,0), (-1, 0)]

        # find all the '0's in the matrix
        # nearest dist to 0 from a 0-cell is 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r,c,0))
                    seen.add((r,c))
        
        # bfs
        while queue:
            r, c, steps = queue.popleft()
            for dx, dy in d:
                nx_r, nx_c = r+dx, c+dy
                if valid(nx_r,nx_c) and (nx_r,nx_c) not in seen:
                    seen.add((nx_r,nx_c))
                    queue.append((nx_r,nx_c, steps+1)) 
                    mat[nx_r][nx_c] = steps + 1 
        return mat
