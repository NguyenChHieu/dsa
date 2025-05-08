class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0
        h = [(0,True,0,0)]
        while h:
            currDist, one, x, y = heappop(h)
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n:
                    newDist = max(currDist, moveTime[nx][ny]) + (1 if one else 2)
                    if newDist < dist[nx][ny]:
                        dist[nx][ny] = newDist
                        heappush(h, (newDist, False if one else True, nx, ny))
        return int(dist[m-1][n-1])
