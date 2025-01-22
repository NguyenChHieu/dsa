class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """
        bfs
        """
        m = len(isWater)
        n = len(isWater[0])
        q = deque()
        seen = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j, 0))
                    seen.add((i, j))
                    isWater[i][j] = 0

        while q:
            r, c, h = q.popleft()
            for dx, dy in dirs:
                nx, ny = r + dx, c + dy
                if valid(nx, ny) and (nx, ny) not in seen:
                    isWater[nx][ny] = h + 1
                    seen.add((nx, ny))
                    q.append((nx, ny, h + 1))
        return isWater

