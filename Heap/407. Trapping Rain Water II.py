class Solution:
    """
    We should process it from the boundaries, because they
    acts as the primary boundary for the inner cells, and they
    cant stored any water.

    Visit all the boundaries, push to a min heap for further processing.

    Pop the cells 1 by 1 then update the minBoundary (max of curr_height 
    with minBoundary - this is because when we encounter a 

        + smaller height -> some water can be trapped 
        + higher height -> all the height <= curr height have been processed for now

    , check the adjacent cells to add any cell to the 
    heap that hasnt been visited.
    """
    def trapRainWater(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        h = []
        visited = [[False for _ in range(C)] for _ in range(R)]

        # visited all boundary cells
        for i in range(R):
            for j in range(C):
                if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                    heappush(h, (grid[i][j], i, j))
                    visited[i][j] = True

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minBoundary = 0
        ans = 0
        while h:
            curr_h, r, c = heappop(h)
            minBoundary = max(minBoundary, curr_h)

            for dx, dy in dirs: # search for unvisited nb
                nR, nC = r + dx, c + dy
                if 0 <= nR < R and 0 <= nC < C and not visited[nR][nC]:
                    if grid[nR][nC] < minBoundary: # trapped water
                        ans += minBoundary - grid[nR][nC]
                    heappush(h, (grid[nR][nC], nR, nC))
                    visited[nR][nC] = True
        return ans

        
