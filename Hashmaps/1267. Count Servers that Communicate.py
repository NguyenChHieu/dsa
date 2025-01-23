class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        r_count = [0] * m
        c_count = [0] * n
        ans = 0

        # count number of servers in a r/c
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r_count[i] += 1
                    c_count[j] += 1

        # if count of r/c > 1 -> at least 2 servers are connected
        # any of the latter servers will be connected too.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (r_count[i] > 1 or c_count[j] > 1):
                    ans += 1
        return ans

        
