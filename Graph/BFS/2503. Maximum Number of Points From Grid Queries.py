class Solution:
    # sort the queries, and expand from top left corner.
    # leverage the "already computed" values and keep track
    # of the boundaries ~ the cells where last query does not
    # satisfy grid[i][j] < queries[k]
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        q = deque([(0, 0)])
        seen = {(0,0)}
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        prev_q_count = 0
        s_q = sorted(queries)
        mapping = {}

        for s in s_q:
            if s in mapping:
                continue
            boundary = deque()
            count = prev_q_count
            while q:
                i, j = q.popleft()
                if s > grid[i][j]:
                    count += 1
                    for dx, dy in dirs:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in seen:
                            seen.add((nx,ny))
                            q.append((nx, ny))
                else:
                    boundary.append((i, j))
            mapping[s] = count
            q = boundary
            prev_q_count = count

        ans = []
        for q in queries:
            if q in mapping:
                ans.append(mapping[q])
            else:
                ans.append(0)
        return ans
