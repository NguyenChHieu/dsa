class Solution:
    # dfs returns: total land cells + whether to add it
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j, bound):
            touch_bound = bound or i == 0 or i == m-1 or j == 0 or j == n-1
            total = 1
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                # valid, is land, not seen yet
                if 0 <= nx < m and 0 <= ny < n \
                        and grid[nx][ny] == 1 \
                        and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    sub_count, sub_bound = dfs(nx, ny, touch_bound)
                    total += sub_count
                    touch_bound = touch_bound or sub_bound
            return total if not touch_bound else 0, touch_bound

        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    cnt, _ = dfs(r, c, False)
                    ans += cnt
        return ans

        # theres a better way: find all boundary land cells, add them to the queue
        # mark any of the adjacent cells to 0. then just return the sum of the whole matrix.

