class Solution:
    # def minCost(self, grid: List[List[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])

        # def valid(r, c):
        #     return 0 <= r < m and 0 <= c < n

        # def nxt(r, c, val):
        #     if val == 1:
        #         if valid(r, c + 1):
        #             return r, c + 1
        #     elif val == 2:
        #         if valid(r, c - 1):
        #             return r, c - 1
        #     elif val == 3:
        #         if valid(r + 1, c):
        #             return r + 1, c
        #     else:
        #         if valid(r - 1, c):
        #             return r - 1, c

        # dirs = [1, 2, 3, 4]
        # seen = {(0, 0, grid[0][0])}
        # queue = deque([(0, 0, grid[0][0], 0)])
        # ans = float('inf')
        # while queue:
        #     r, c, val, cost = queue.popleft()
        #     if r == m-1 and c == n-1:
        #         ans = min(ans, cost)
        #     for d in dirs:
        #         nxt_cell = nxt(r, c, d)
        #         if nxt_cell:
        #             if (r, c, d) not in seen:
        #                 seen.add((r, c, d))
        #                 queue.append((r, c, d, cost + 1))

        #     nxt_cell = nxt(r, c, val)
        #     if nxt_cell:
        #         nxt_r, nxt_c = nxt_cell
        #         if (nxt_r, nxt_c, grid[nxt_r][nxt_c]) not in seen:
        #             seen.add((nxt_r, nxt_c, grid[nxt_r][nxt_c]))
        #             queue.append((nxt_r, nxt_c, grid[nxt_r][nxt_c], cost))
        # return ans


    """
    djikstra - correct dir = wight 0, else weight 1.
    """
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        h = [(0,0,0)] # cost, r,c
        dist = defaultdict(lambda : float('inf'))
        dist[(0,0)] = 0

        while h:
            cost, r, c = heappop(h)

            if r == m-1 and c == n-1:
                return cost

            for i, (dr,dc) in enumerate(dirs):
                nxt_r, nxt_c = r + dr, c+ dc
                if m > nxt_r >= 0 and n > nxt_c >= 0:
                    new_cost = cost + 0 if i+1 == grid[r][c] else cost + 1 # same dir with arrow = +0
                    if new_cost < dist[(nxt_r,nxt_c)]:
                        heappush(h, (new_cost, nxt_r, nxt_c))
                        dist[(nxt_r, nxt_c)] = new_cost
