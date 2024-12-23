class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # keep the graph as having 2 separate edge sets. Then perform 
        # normal bfs, when adding a new move make sure to flip the colors
        RED = 'R'
        BLUE = 'B'

        graphs = defaultdict(lambda: defaultdict(list))
        # 2 diff edge sets in graph
        for x, y in redEdges:
            graphs[RED][x].append(y)
        for x, y in blueEdges:
            graphs[BLUE][x].append(y)

        ans = [float('inf')]*n
        q = deque([(0,RED,0), (0, BLUE, 0)])
        seen = {(0, RED), (0,BLUE)}

        while q:
            node, color, steps = q.popleft()
            ans[node] = min(ans[node],steps) # update ans

            for nb in graphs[color][node]:
                next_color = RED if color == BLUE else BLUE # flip
