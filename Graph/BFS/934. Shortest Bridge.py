class Solution:
    # dfs to find first island - found
    # then throw "seen" to bfs, this would
    # find all adjacent water cells, once
    # it reaches the other island, it guarantees
    # to be the smallest step (bfs feature)
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if 0 <= x < n and 0 <= y < n and (x, y) not in seen and grid[x][y] == 1:
                seen.add((x, y))
                grid[x][y] = 2
                for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                    dfs(x+dx, y+dy)

        def bfs():
            q = deque(seen)
            steps = 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
                            if grid[nx][ny] == 1:
                                return steps
                            q.append((nx, ny))
                            seen.add((nx, ny))
                steps += 1

        n = len(grid)
        seen = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()
        # def neighbor(x, y, target, seen):
        #     dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #     nb = []
        #     for dx, dy in dirs:
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < n \
        #                 and 0 <= ny < n \
        #                 and grid[nx][ny] == target \
        #                 and (nx, ny) not in seen:
        #             seen.add((nx, ny))
        #             nb.append((nx, ny))
        #     return nb

        # def dfs(x, y, mark, seen):
        #     grid[x][y] = mark
        #     nb = neighbor(x, y, 1, seen)
        #     for nx, ny in nb:
        #         dfs(nx, ny, mark, seen)

        # def bfs(x, y, target):
        #     dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #     q = deque([(x, y, 0)])
        #     seen = {(x,y)}
        #     while q:
        #         x, y, step = q.popleft()
        #         if grid[x][y] == target:
        #             return step
        #         for dx, dy in dirs:
        #             nx, ny = x + dx, y + dy
        #             if 0 <= nx < n \
        #                 and 0 <= ny < n \
        #                     and (nx, ny) not in seen:
        #                 seen.add((nx, ny))
        #                 q.append((nx, ny, step + 1))
        #     return -1

        # n = len(grid)
        # fst = True
        # i1 = set()
        # i2 = set()
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             if fst:
        #                 i1.add((i, j))
        #                 dfs(i, j, 2, i1)
        #                 fst = False
        #             else:
        #                 i2.add((i, j))
        #                 dfs(i, j, 3, i2)
        # start = i2 if len(i2) <= len(i1) else i1
        # target = 2 if len(i2) <= len(i1) else 3  # 3 for i2, 2 for i1
        # bounds = set()
        # for x, y in start:
        #     neighbor(x, y, 0, bounds)

        # ans = 101
        # for x, y in bounds:
        #     ans = min(ans, bfs(x, y, target))
        # return ans
            
