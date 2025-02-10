class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # bs on s space, with effort k is "k, to check if theres a path, use dfs"
        l = 0
        r = max(max(h) for h in heights)
        drs = [(0,1), (0,-1), (1,0), (-1,0)]

        def valid(r,c):
            return 0 <= r < len(heights) and 0 <= c < len(heights[0])
        
        def dfs(x, y, k,seen):
            if (x,y) == (len(heights)-1, len(heights[0]) - 1):
                return True

            for dx, dy in drs:
                nx,ny = x+dx, y+dy
                if valid(nx,ny) and \
                (nx,ny) not in seen and \
                abs(heights[nx][ny] - heights[x][y]) <= k:
                    seen.add((nx,ny))
                    if dfs(nx,ny,k,seen):
                        return True
            return False

        while l <= r:
            mid = (l+r) //2 
            seen = {(0,0)}
            if dfs(0,0,mid, seen):
                r = mid - 1
            else:
                l = mid + 1
        return l
            
