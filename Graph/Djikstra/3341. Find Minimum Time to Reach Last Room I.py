class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0,0,0)]
        while heap:
            currTime, x, y  = heappop(heap)
            for dx, dy in [(0,1), (0,-1), (1,0),(-1,0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n:
                    ndist = max(currTime, moveTime[nx][ny]) +1
                    if ndist < dist[nx][ny]:
                        dist[nx][ny] = ndist
                        heappush(heap, (ndist,nx,ny))
        return int(dist[m-1][n-1])
