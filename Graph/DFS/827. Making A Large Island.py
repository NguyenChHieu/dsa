class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        Precompute the islands - traverse through 0's to 
        check its neighbors (make sure to not reuse an island twice)

        # Traverse through 1's - change it to = label, and return the final size.
        
        Also check the case when the grid full of 1s.
        """


        n = len(grid)
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def valid(r, c):
            return 0 <= r < n and 0 <= c < n

        # can do grid[r][c] = label and size[label] = {total_size}, then when traverse check if grid[r][c] == 1 to account for the cell
        def dfs(r, c, seen):
            ans = 1
            for dx, dy in dirs:
                nx, ny = r + dx, c + dy
                if valid(nx, ny):
                    if grid[nx][ny] == 1:
                        if (nx, ny) not in seen:
                            seen.add((nx, ny))
                            area, _ = dfs(nx, ny, seen)
                            ans += area
            return ans, seen

        def check(r, c):
            ans = 1
            marked = set()
            for dx, dy in dirs:
                nx,ny = r+dx, c+dy
                if valid(nx,ny):
                    area, island_id = island.get((nx,ny),(0,0))
                    if island_id not in marked:
                        ans += area
                        marked.add(island_id)
            return ans

        island = {}
        ids = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    if (r, c) not in island:
                        area, cells = dfs(r, c, {(r, c)})
                        for cell in cells:
                            island[cell] = (area, ids)
                        ids += 1
        res = 0
        for area, ids in island.values():
            res = max(area, res)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    res = max(res, check(r,c))
        return res

